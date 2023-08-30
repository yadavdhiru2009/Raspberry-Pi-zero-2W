#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used to measure the distance of the Object using the
 Ultrsonic sensor
"""
from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(23, 24, max_distance=1, threshold_distance=0.2)
led = LED(16)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()
