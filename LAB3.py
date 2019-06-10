from machine import Pin
from time import sleep
led = Pin(16, Pin.OUT)
led.off()
switch = Pin(0, Pin.IN, Pin.PULL_UP)
while True:
    if not switch.value():
        led.value(not led.value())
        sleep(.5)
        
