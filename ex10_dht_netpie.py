# Example 10: DHT Sensor with Wokwi on NETPIE

import dht
from machine import Pin # Required for dht library
import ujson
import network
from time import sleep_ms
from umqtt.simple import MQTTClient

SSID = 'Wokwi-GUEST'
PASS = ''
BROKER = 'mqtt.netpie.io'
CLIENT_ID = ''  # Copied from your device
TOKEN = ''      # Copied from your device
SECRET = ''     # Leave Blank

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID,PASS) # Start Connecting
print('WiFi ', end='')
while not wlan.isconnected():
    print('.', end='')
    sleep_ms(500)
    print(' connected to', wlan.ifconfig()[0])

# Connect to MQTT broker
client = MQTTClient(CLIENT_ID,BROKER,user=TOKEN,password=SECRET)
try:
    client.connect()
    print('MQTT Connected')
except:
    print('MQTT Error')

sensor = dht.DHT22(Pin(15))

while True:
    sensor.measure()
    data = {'Temp': sensor.temperature(),
            'RH': sensor.humidity()
            }
    payload = ujson.dumps({'data':data})
    print(payload)
    client.publish('@shadow/data/update', payload)
    sleep_ms(1500)