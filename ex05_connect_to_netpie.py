# Example 5: Connect Device to NETPIE

import network
import time
from umqtt.simple import MQTTClient

WiFi_SSID = 'Wokwi-GUEST'
WiFi_PASS = ''

MQTT_BROKER    = 'mqtt.netpie.io'
MQTT_CLIENT_ID = 'DEVICE CLIENT ID' # Copied from your device
MQTT_TOKEN     = 'DEVICE TOKEN'
MQTT_SECRET    = '' 

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)   # Set WiFi Mode to Station
wlan.active(True)

wlan.connect(WiFi_SSID,WiFi_PASS)  # Start Connecting
print('WiFi ', end='')
while not wlan.isconnected():
  print('.', end='')
  time.sleep(0.5)
print(' connected to', wlan.ifconfig()[0]) # Print connected IP Address

# Connect to MQTT broker
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_TOKEN, password=MQTT_SECRET)
try:
  client.connect()
  print('MQTT Connected')
except:
  print('MQTT Error')
