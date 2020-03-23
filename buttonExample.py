#https://microbit.org/guide/python/
#https://python.microbit.org/v/2.0
#https://www.python.org/community/microbit/
#https://github.com/bbcmicrobit/micropython

from microbit import *

a=1
for w in range(100):
    for l in range(4):
        display.set_pixel(l,w%5,a)
        display.set_pixel(w%5,l,a)
        sleep(w%50)
        a+=1
        if(a==10):
            a=1
            display.clear()

x=0
y=0
time=0
while time < 500:
    time+=1
    if button_a.is_pressed():
        x-=1
    if button_b.is_pressed():
        x+=1
    if button_a.is_pressed() and button_b.is_pressed():
        y+=1
    if not button_a.is_pressed() and not button_b.is_pressed():
        y-=1
    if x>4:
        x=0
    if x<0:
        x=4
    if y>4:
        y=0
    if y<0:
        y=4
    display.set_pixel(x,y,9)
    sleep(85)
    display.clear()
  
while True:
    a=1
    for w in range(100):
        for l in range(4):
            display.set_pixel(l,w%5,a)
            display.set_pixel(w%5,l,a)
            display.set_pixel(l,l,a)
            display.set_pixel(w%5,w%5,a)
            sleep(w%50)
            a+=1
            if(a==10):
                a=1
