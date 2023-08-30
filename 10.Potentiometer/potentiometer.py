#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used Check value of the Potentiometer using RPI 2W
"""
from gpiozero import MCP3008

pot = MCP3008(channel=0)

while True:
    print(pot.value)
