# Example 9: Basic DHT Sensor with JSON output

import dht
from machine import Pin  # Required for dht library
from time import sleep
import ujson

sensor = dht.DHT22(Pin(15))

while True:
    sensor.measure()
    
    msg_dic = {
        "Temp": sensor.temperature(),
        "RH": sensor.humidity()
    }
    msg_json = ujson.dumps(msg_dic)

    print(msg_json)

    sleep(1)
