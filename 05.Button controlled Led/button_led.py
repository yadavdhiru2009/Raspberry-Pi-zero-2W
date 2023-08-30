"""
 Author :Dharmendra Kumar Yadav
 this code is turn on led on and off by using the button
"""
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
