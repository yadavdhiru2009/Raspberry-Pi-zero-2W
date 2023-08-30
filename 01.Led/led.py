#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used control the Led at pin no 17
"""
from gpiozero import LED
from time import sleep

red = LED(17)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
