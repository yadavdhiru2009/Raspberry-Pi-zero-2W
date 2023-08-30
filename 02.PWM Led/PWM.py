#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used control the Led at pin no 17 using PWM
"""
from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.5  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)
