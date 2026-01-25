# Example 8: Basic DHT Sensor

import dht
from machine import Pin  # Required for dht library
from time import sleep

sensor = dht.DHT22(Pin(15))

while True:
  sensor.measure()
  print(sensor.temperature(),sensor.humidity())
  sleep(1)
