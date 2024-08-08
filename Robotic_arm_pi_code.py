# Author: Jeffrey Hernandez, with libraries from Kevin McAleer
# This code is to control a robotic arm with a Raspberry Pi Pico, a PCA9685 16 channel servo driver and SG90 servos
from pca9685 import PCA9685
from machine import I2C, Pin, ADC
from servo import Servos
import time

# Initialize I2C and PCA9685
sda = Pin(0)
scl = Pin(1)
i2c = I2C(id=0, sda=sda, scl=scl)
pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

# Initialize Joystick (Assuming X and Y are connected to ADC pins)
joystick_x = ADC(Pin(26))
joystick_y = ADC(Pin(27))
button = Pin(16, Pin.IN, Pin.PULL_UP)

# Initialize Potentiometer (Assuming it is connected to an ADC pin)
potentiometer = ADC(Pin(28))

# Constants for deadzone and filtering
DEADZONE = 2000
FILTER_SAMPLES = 5

def read_joystick():
    x = joystick_x.read_u16()  # Read X-axis
    y = joystick_y.read_u16()  # Read Y-axis
    return x, y

def read_potentiometer():
    return potentiometer.read_u16()

def read_joystick_button():
    return button.value()

def map_value(value, from_low, from_high, to_low, to_high):
    # Maps an input value from one range to another range
    return to_low + (value - from_low) * (to_high - to_low) / (from_high - from_low)

def apply_deadzone(value, center, deadzone):
    if abs(value - center) < deadzone:
        return center
    return value

def filter_value(read_function, samples):
    values = [read_function() for _ in range(samples)]
    return sum(values) // samples

# Initialize last positions with a default position
last_servo1_angle = 90
last_servo2_angle = 90
last_servo3_angle = 90
last_servo4_angle = 90

while True:
    # Read joystick and potentiometer values with filtering
    x = filter_value(lambda: apply_deadzone(joystick_x.read_u16(), 32768, DEADZONE), FILTER_SAMPLES)
    y = filter_value(lambda: apply_deadzone(joystick_y.read_u16(), 32768, DEADZONE), FILTER_SAMPLES)
    pot = filter_value(potentiometer.read_u16, FILTER_SAMPLES)
    joystick_button = read_joystick_button()

    # Check if inputs are outside the deadzone
    if x != 32768:
        last_servo1_angle = map_value(x, 0, 65535, 0, 180)
    if y != 32768:
        last_servo2_angle = map_value(y, 0, 65535, 0, 180)
    last_servo3_angle = map_value(pot, 0, 65535, 0, 180)  # Potentiometer always considered
    last_servo4_angle = map_value(joystick_button, 0, 1, 0, 180)  # Button as binary

    # Set servo positions
    servo.position(index=12, degrees=last_servo1_angle)  # Base servo
    servo.position(index=13, degrees=last_servo2_angle)  # Arm servo
    servo.position(index=14, degrees=last_servo3_angle)  # Palm servo
    servo.position(index=15, degrees=last_servo4_angle)  # Claw Servo

    # Print the current angles of the servos
    print(f"Servo 1 Angle: {last_servo1_angle}")
    print(f"Servo 2 Angle: {last_servo2_angle}")
    print(f"Servo 3 Angle: {last_servo3_angle}")
    print(f"Servo 4 Angle: {last_servo4_angle}")
    print("-" * 30)  # Separator for readability

    time.sleep(0.1)  # Small delay to prevent excessive I2C communication
