"""
Robotic Arm Control System

This script controls a robotic arm using a Raspberry Pi Pico, a PCA9685 16-channel servo driver,
and SG90 servos. The arm is controlled via an analog joystick module with a push button and a potentiometer.

Author: Jeffrey Hernandez (original), with improvements and documentation by Claude
Libraries: Kevin McAleer (pca9685 and servo modules)

Hardware:
- Raspberry Pi Pico
- PCA9685 16-channel servo driver
- SG90 servos
- Analog joystick module with push button
- Potentiometer

Dependencies:
- pca9685
- machine
- servo
- time
"""

from pca9685 import PCA9685
from machine import I2C, Pin, ADC
from servo import Servos
import time

# Constants
DEADZONE = 2000
FILTER_SAMPLES = 5
SMOOTHING_FACTOR = 0.1
UPDATE_INTERVAL = 0.05  # seconds

# Pin Configurations
SDA_PIN = 0
SCL_PIN = 1
JOYSTICK_X_PIN = 26
JOYSTICK_Y_PIN = 27
JOYSTICK_BUTTON_PIN = 16
POTENTIOMETER_PIN = 28

# Servo Configurations
BASE_SERVO_INDEX = 12
ARM_SERVO_INDEX = 13
PALM_SERVO_INDEX = 14
CLAW_SERVO_INDEX = 15

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def update(self, setpoint, current_value):
        error = setpoint - current_value
        self.integral += error
        derivative = error - self.previous_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output

class RoboticArm:
    def __init__(self):
        # Initialize I2C and PCA9685
        i2c = I2C(id=0, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN))
        self.pca = PCA9685(i2c=i2c)
        self.servo = Servos(i2c=i2c)

        # Initialize controls
        self.joystick_x = ADC(Pin(JOYSTICK_X_PIN))
        self.joystick_y = ADC(Pin(JOYSTICK_Y_PIN))
        self.button = Pin(JOYSTICK_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
        self.potentiometer = ADC(Pin(POTENTIOMETER_PIN))

        # Adjust servo ranges and center positions
        self.servo_ranges = {
            BASE_SERVO_INDEX: (20, 160, 90),  # (min, max, center)
            ARM_SERVO_INDEX: (0, 180, 90),
            PALM_SERVO_INDEX: (0, 180, 90),
            CLAW_SERVO_INDEX: (0, 180, 90)
        }

        # Initialize last positions and smoothed values
        self.last_servo_angles = [self.servo_ranges[i][2] for i in [BASE_SERVO_INDEX, ARM_SERVO_INDEX, PALM_SERVO_INDEX, CLAW_SERVO_INDEX]]
        self.last_values = [32768, 32768, 32768, 0]  # x, y, pot, button
        
        # Add movement speed limitations
        self.max_speed = 2  # Maximum degrees of movement per update

        # Initialize PID controllers for each servo
        self.pid_controllers = {
            index: PIDController(kp=0.5, ki=0.1, kd=0.1) for index in self.servo_ranges
        }

    def read_joystick(self):
        """Read joystick X and Y values."""
        return self.joystick_x.read_u16(), self.joystick_y.read_u16()

    def read_potentiometer(self):
        """Read potentiometer value."""
        return self.potentiometer.read_u16()

    def read_joystick_button(self):
        """Read joystick button state."""
        return self.button.value()

    @staticmethod
    def map_value(value, from_low, from_high, to_low, to_high):
        """Map an input value from one range to another."""
        return to_low + (value - from_low) * (to_high - to_low) / (from_high - from_low)

    @staticmethod
    def apply_deadzone(value, center, deadzone):
        """Apply a deadzone to a value."""
        return center if abs(value - center) < deadzone else value

    def filter_value(self, read_function, samples):
        """Apply a simple moving average filter."""
        return sum(read_function() for _ in range(samples)) // samples

    @staticmethod
    def smooth_value(new_value, last_value, factor):
        """Apply exponential smoothing to a value."""
        return (factor * new_value) + ((1 - factor) * last_value)

    def map_to_servo_range(self, value, servo_index):
        """Map input value to the specific servo's range."""
        min_angle, max_angle, center = self.servo_ranges[servo_index]
        return self.map_value(value, 0, 65535, min_angle, max_angle)

    def update_servo_positions(self):
        """Update servo positions based on control inputs with PID control."""
        # Read and process control inputs
        raw_x, raw_y = self.read_joystick()
        raw_x = self.apply_deadzone(raw_x, 32768, DEADZONE)
        raw_y = self.apply_deadzone(raw_y, 32768, DEADZONE)
        raw_pot = self.read_potentiometer()
        button = self.read_joystick_button()

        # Apply filtering and smoothing
        smoothed_values = [
            self.smooth_value(self.filter_value(lambda: raw_x, FILTER_SAMPLES), self.last_values[0], SMOOTHING_FACTOR),
            self.smooth_value(self.filter_value(lambda: raw_y, FILTER_SAMPLES), self.last_values[1], SMOOTHING_FACTOR),
            self.smooth_value(raw_pot, self.last_values[2], SMOOTHING_FACTOR),
            button
        ]

        # Update last values
        self.last_values = smoothed_values

        # Map smoothed values to servo angles
        target_angles = [
            self.map_to_servo_range(smoothed_values[0], BASE_SERVO_INDEX),
            self.map_to_servo_range(smoothed_values[1], ARM_SERVO_INDEX),
            self.map_to_servo_range(smoothed_values[2], PALM_SERVO_INDEX),
            180 if smoothed_values[3] == 0 else 0  # Invert button logic for claw
        ]

        # Apply PID control and limit movement speed
        new_angles = []
        servo_indices = [BASE_SERVO_INDEX, ARM_SERVO_INDEX, PALM_SERVO_INDEX, CLAW_SERVO_INDEX]
        for index, last, target in zip(servo_indices, self.last_servo_angles, target_angles):
            pid_output = self.pid_controllers[index].update(target, last)
            new_angle = last + max(min(pid_output, self.max_speed), -self.max_speed)
            new_angle = max(min(new_angle, self.servo_ranges[index][1]), self.servo_ranges[index][0])
            new_angles.append(new_angle)
            self.servo.position(index=index, degrees=new_angle)

        # Update last angles
        self.last_servo_angles = new_angles

    def print_servo_angles(self):
        """Print the current angles of the servos."""
        servo_names = ["Base", "Arm", "Palm", "Claw"]
        for name, angle in zip(servo_names, self.last_servo_angles):
            print(f"{name} Servo Angle: {angle:.2f}")
        print("-" * 30)

    def run(self):
        """Main control loop."""
        while True:
            self.update_servo_positions()
            self.print_servo_angles()
            time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    arm = RoboticArm()
    arm.run()