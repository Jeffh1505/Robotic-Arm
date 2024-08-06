#Author: Jeffrey Hernandez, with libraries from Kevin McAleer
#This code is to control a robotic arm with a Raspberry Pi Pico, a PCA9685 16 channel servo driver and SG90 servos
from pca9685 import PCA9685
# from picocat import Servos
from machine import I2C, Pin
from servo import Servos

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)
pca = PCA9685(i2c=i2c)
# pca.i2c = i2c
servo = Servos(i2c=i2c)

while True:
    claw_servo = servo.position(index=15, degrees=180)