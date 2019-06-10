from machine import Pin, PWM
from time import sleep
n = 0
while n < 10:
    print(n)
    led = PWM(Pin(5), freq=500, duty=(n*100))
    n = n + 1
    if n == 10:
        n = 0
    sleep(.5)
    
