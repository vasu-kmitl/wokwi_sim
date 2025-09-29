###########################################
# Ex.3: Publush on HiveMQ
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

import network
import time
from umqtt.simple import MQTTClient

SSID = 'Wokwi-GUEST'
PASS = ''

BROKER    = 'broker.hivemq.com'
CLIENT_ID = 'vasu-007' # Change to a unique name to avoid collision

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID,PASS)
print('WiFi ', end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)
print(' connected to', wlan.ifconfig()[0])

# Connect to MQTT broker
client = MQTTClient(CLIENT_ID, BROKER)
try:
    client.connect()
    print('MQTT Connected')
except:
    print('MQTT Error')

i = 0
while True:
    client.publish('ae_iot/vasu/temp', str(i))  # Publish here!!!
    print('Published:', i)
    time.sleep(3)
    i = i+1

# Check result on https://www.hivemq.com/demos/websocket-client/