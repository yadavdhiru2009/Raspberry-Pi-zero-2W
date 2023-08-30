#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used control the Motion using raspberry pi 2w
"""
from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(4)
led = LED(16)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()
