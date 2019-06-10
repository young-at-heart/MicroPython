from time import sleep
from machine import Pin
led = Pin(16, Pin.OUT)
switch = Pin(0, Pin.IN, Pin.PULL_UP)
while True:
    state = switch.value()
    if state > 0:
        led.off()
    else:
        led.on()
        
