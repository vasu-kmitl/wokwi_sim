# Example 5: Connect Device to NETPIE

import network
from time import sleep_ms
from umqtt.simple import MQTTClient

SSID = 'Wokwi-GUEST'
PASS = ''

BROKER    = 'mqtt.netpie.io'
CLIENT_ID = 'DEVICE CLIENT ID' # Copied from your device
TOKEN     = 'DEVICE TOKEN'
SECRET    = '' 

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASS)
print('WiFi ', end='')
while not wlan.isconnected():
  print('.', end='')
  sleep_ms(500)
print(' connected to', wlan.ifconfig()[0])

# Connect to MQTT broker
client = MQTTClient(CLIENT_ID, BROKER, user=TOKEN, password=SECRET)
try:
  client.connect()
  print('MQTT Connected')
except:
  print('MQTT Error')
