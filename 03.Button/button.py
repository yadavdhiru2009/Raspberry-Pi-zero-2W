"""
 Author :Dharmendra Kumar Yadav
 this code is used press the Button and See output on the Terminal
"""
from gpiozero import Button

button = Button(2)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
