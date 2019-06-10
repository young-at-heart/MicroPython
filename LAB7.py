from machine import ADC
from time import sleep
adc = ADC(39)
while True:
    print(adc.read())
    sleep(1)
    
