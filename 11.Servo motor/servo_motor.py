#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used control the single Servo motor using the RPI2w Zero

"""
from gpiozero import Servo
from time import sleep

servo = Servo(17)

while True:
    servo.min()
    sleep(2)
    servo.mid()
    sleep(2)
    servo.max()
    sleep(2)
