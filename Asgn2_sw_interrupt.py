###########################################
# Asgn.2: SW with Interrupt
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
# Ref: https://docs.micropython.org/en/latest/library/machine.Pin.html
###########################################

from machine import Pin, Timer
from time import ticks_ms, ticks_diff

sw = Pin(2, Pin.IN, Pin.PULL_UP)   # button -> GND

last = sw.value()                  # 1 = OFF, 0 = ON
debounce_ms = 40
tmr = Timer(0)

def sw_read(t):
    global last
    sw_read = sw.value()
    if sw_read != last:
        last = sw_read
        if sw_read == 0:
            print('ON')
        else:
            print('OFF')

def _irq(pin):
    tmr.init(mode=Timer.ONE_SHOT, period=debounce_ms, callback=sw_read)

sw.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=_irq)

while True:
    pass
