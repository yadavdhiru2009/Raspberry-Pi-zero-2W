
#!/usr/bin/python
"""
 Author :Dharmendra Kumar Yadav
 this code is used Check Control the Motor using Raspberry pi 2w
"""
from gpiozero import Motor
from time import sleep

motor = Motor(forward=4, backward=14)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)
