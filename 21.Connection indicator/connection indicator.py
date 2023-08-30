#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used to Show the netwok Connection based on
 the device connected or not
 
"""
from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause

green = LED(17)
red = LED(18)

google = PingServer('google.com')

google.when_activated = green.on
google.when_deactivated = green.off
red.source = negated(green)

pause()
