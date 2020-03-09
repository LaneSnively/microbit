#https://microbit.org/guide/python/
#https://python.microbit.org/v/2.0
#https://www.python.org/community/microbit/
#https://github.com/bbcmicrobit/micropython

from microbit import *

display.set_pixel(0,0,9)
x=0
y=0
while True:
    if button_a.is_pressed():
        x=x-1
    elif button_b.is_pressed():
        x=x+1
    if x>4:
        x=0
    if x<0:
        x=4
    if pin0.is_touched():
        y=y-1
    elif pin1.is_touched():
        y=y+1
    if y>4:
        y=0
    if y<0:
        y=4
    display.set_pixel(x,y,9)
    sleep(75)
    display.clear()
