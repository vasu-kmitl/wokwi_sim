###########################################
# Ex.4: Subscribe on HiveMQ
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

import network
import time
from umqtt.simple import MQTTClient

SSID = 'Wokwi-GUEST'
PASS = ''

CLIENT_ID = 'vasu-007' # Change to a unique name to avoid collision
BROKER    = 'broker.hivemq.com'

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASS)
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

# Callback function for responding to the subscribed topics
def on_message(topic, msg):
    incoming_message = msg.decode('utf8')
    print('{}: {}'.format(topic, incoming_message))

client.set_callback(on_message)         # Attach the CALLBACK routine
client.subscribe('ae_iot/vasu/temp')    # Hook up to a subscribed topic
client.subscribe('ae_iot/vasu/fan')     # Try with wildcards # and +

while True:
    client.check_msg()     # Periodically chack the incoming message

# Now try to publish relevant topics on https://www.hivemq.com/demos/websocket-client/
