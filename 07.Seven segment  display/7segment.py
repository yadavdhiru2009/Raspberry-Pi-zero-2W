#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used show number in 7 segment Display
"""
from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(21, 20, 16, 22, 23, 24, 12, dp=25)

for char in '321GO':
    display.value = char
    sleep(1)

display.off()
