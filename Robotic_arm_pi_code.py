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

# Initialize Potentiometer (Assuming it is connected to an ADC pin)
potentiometer = ADC(Pin(28))

def read_joystick():
    x = joystick_x.read_u16()  # Read X-axis
    y = joystick_y.read_u16()  # Read Y-axis
    return x, y

def read_potentiometer():
    return potentiometer.read_u16()

def map_value(value, from_low, from_high, to_low, to_high):
    # Maps an input value from one range to another range
    return to_low + (value - from_low) * (to_high - to_low) / (from_high - from_low)

while True:
    x, y = read_joystick()
    pot = read_potentiometer()
    
    # Map joystick and potentiometer values to servo angles
    servo1_angle = map_value(x, 0, 65535, 0, 180)  # Adjust range if necessary
    servo2_angle = map_value(y, 0, 65535, 0, 180)  # Adjust range if necessary
    servo3_angle = map_value(pot, 0, 65535, 0, 180)  # Adjust range if necessary

    # Set servo positions
    servo.position(index=0, degrees=servo1_angle)  # Base servo
    servo.position(index=1, degrees=servo2_angle)  # Arm servo
    servo.position(index=2, degrees=servo3_angle)  # Claw servo
    servo.position(index=15, degrees=180)  # Example static position for another servo

    time.sleep(0.1)  # Small delay to prevent excessive I2C communication
