###########################################
# Ex.2: HiveMQ Connection
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

import network
import time
from umqtt.simple import MQTTClient

SSID = 'Wokwi-GUEST'
PASS = ''

BROKER    = 'broker.hivemq.com'
CLIENT_ID = 'vasu-010' # Change to a unique name to avoid collision

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)   # Create a WiFi Station Interface
wlan.active(True)

wlan.connect(SSID, PASS)  # Start Connecting
print('WiFi ', end='')
while not wlan.isconnected():
  print('.', end='')
  time.sleep(0.5)
print(' connected to ', wlan.ifconfig()[0])

# Connect to MQTT broker
client = MQTTClient(CLIENT_ID, BROKER)
try:
    client.connect()
    print('MQTT Connected')
except:
    print('MQTT Error')

