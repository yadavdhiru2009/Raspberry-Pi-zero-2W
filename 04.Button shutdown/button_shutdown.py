#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used to turn of the raspberry pi zero 2w
 using the button at pin no 17
"""
from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(2, hold_time=2)
shutdown_btn.when_held = shutdown

pause()
