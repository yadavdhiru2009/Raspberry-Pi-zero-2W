#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is usedcontrol the motor using the RPI 2W Zero
"""
from gpiozero import Robot
from time import sleep

robot = Robot(left=(4, 14), right=(17, 18))

for i in range(4):
    robot.forward()
    sleep(10)
    robot.right()
    sleep(1)
