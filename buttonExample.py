#https://microbit.org/guide/python/
#https://python.microbit.org/v/2.0
#https://www.python.org/community/microbit/
#https://github.com/bbcmicrobit/micropython

from microbit import *

while True:
    cool()
    game()
    lane()
    snively()

def cool():
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
    
def game():
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
        
def lane():
    display.set_pixel(0,0,9)
    display.clear()
    sleep(85)
    display.set_pixel(0,1,9)
    display.set_pixel(1,1,9)
    display.set_pixel(1,0,9)
    display.clear()
    sleep(85)
    display.set_pixel(0,2,9)
    display.set_pixel(1,2,9)
    display.set_pixel(2,2,9)
    display.set_pixel(2,1,9)
    display.set_pixel(2,0,9)
    display.clear()
    sleep(85)
    display.set_pixel(0,3,9)
    display.set_pixel(1,3,9)
    display.set_pixel(2,3,9)
    display.set_pixel(3,3,9)
    display.set_pixel(3,2,9)
    display.set_pixel(3,1,9)
    display.set_pixel(3,0,9)
    display.clear()
    sleep(85)
    display.set_pixel(0,4,9)
    display.set_pixel(1,4,9)
    display.set_pixel(2,4,9)
    display.set_pixel(3,4,9)
    display.set_pixel(4,4,9)
    display.set_pixel(4,3,9)
    display.set_pixel(4,2,9)
    display.set_pixel(4,1,9)
    display.set_pixel(4,0,9)
    display.clear()
    sleep(85)
    
def snively():
    h=0
    while h<5:
        display.set_pixel(h,h,9)
        for i in range(0,5):
            display.set_pixel(h,i,9)
            display.clear()
            
