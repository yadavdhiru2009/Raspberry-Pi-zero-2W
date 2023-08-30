#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used run a robot we have 4 button named left
 right forward and backward respectively on pressing the button
 the motor run in desired direction
"""
from gpiozero import Robot, Button
from signal import pause

robot = Robot(left=(4, 14), right=(17, 18))

left = Button(26)
right = Button(16)
fw = Button(21)
bw = Button(20)

fw.when_pressed = robot.forward
fw.when_released = robot.stop

left.when_pressed = robot.left
left.when_released = robot.stop

right.when_pressed = robot.right
right.when_released = robot.stop

bw.when_pressed = robot.backward
bw.when_released = robot.stop

pause()
