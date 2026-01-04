###########################################
# Task 3: Blinking LED
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

from machine import Pin
from time import sleep_ms

LED = Pin(15,Pin.OUT)

while True:
    LED.on()
    print(LED.value())
    sleep_ms(1000)
    LED.off()
    print(LED.value())
    sleep_ms(1000)
