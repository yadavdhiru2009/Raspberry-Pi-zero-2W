#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used Check Light Depended Resistor sensor
"""
from gpiozero import LightSensor

sensor = LightSensor(18)

while True:
    sensor.wait_for_light()
    print("It's light! :)")
    sensor.wait_for_dark()
    print("It's dark :(")
