###########################################
# Asgn.1: Basic ADC
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(34))

while True:
    digital = adc.read()
    voltage = digital/4096 * 3.3
    print(digital, voltage)
    sleep(3) 
