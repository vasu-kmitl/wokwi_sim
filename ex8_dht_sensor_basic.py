# Example 8: Basic DHT Sensor

import dht
from machine import Pin # Required for dht library
from time import sleep_ms
sensor = dht.DHT22(Pin(15))

while True:
    sensor.measure()
    print(sensor.temperature(),sensor.humidity())
    sleep_ms(1500)