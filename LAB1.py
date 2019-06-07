from time import sleep
from machine import Pin
p = Pin(16, Pin.OUT)
while True:
  p.on()
  sleep(1)
  print('turn on led')
  p.off()
  sleep(1)
  print('turn off led')
  
