# Example 9: Basic DHT Sensor using JSON

import dht
from machine import Pin # Required for dht library
from time import sleep_ms
import ujson

sensor = dht.DHT22(Pin(15))

while True:
    sensor.measure()
    message = ujson.dumps({
        "Temp": sensor.temperature(),
        "RH": sensor.humidity()
    })
    print(message)
    sleep_ms(1000)