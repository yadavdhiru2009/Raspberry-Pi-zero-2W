#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used control the motion of camera by pressing the Button
"""
from gpiozero import Button
from picamera import PiCamera

button = Button(2)
camera = PiCamera()

camera.start_preview()
frame = 1
while True:
    button.wait_for_press()
    camera.capture('/home/pi/frame%03d.jpg' % frame)
    frame += 1
