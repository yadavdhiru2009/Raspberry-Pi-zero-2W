#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used control the LedBoard graph at pin no (5, 6, 13, 19, 26)
"""
from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(5, 6, 13, 19, 26)

leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value = (1, 0, 1, 0, 1)
sleep(1)
leds.blink()

pause()
