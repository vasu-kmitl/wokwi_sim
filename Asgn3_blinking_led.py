###########################################
# Asgn.3: Blinking LED
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

from machine import Pin
from time import sleep_ms

outPin = Pin(15,Pin.OUT)

while True:
    outPin.on()
    print(outPin.value())
    sleep_ms(1000)
    outPin.off()
    print(outPin.value())
    sleep_ms(1000)
