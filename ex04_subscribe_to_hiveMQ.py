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

CLIENT_ID = 'vasu-008' # Change to a unique name to avoid collision
                       # Use different ID from Ex.3 to avoid collapse 
BROKER    = 'broker.hivemq.com'

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
client = MQTTClient(CLIENT_ID,BROKER)
try:
    client.connect()
    print('MQTT Connected')
except:
    print('MQTT Error')

# CALLBACK function, automatically run when getting a subscribed topic
def on_message(topic, msg):
    topic = topic.decode('utf8')
    msg   = msg.decode('utf8')
    print(topic, ':', msg)
    # Add coads as needed by fiterling topic and msg for spefic purposes  

client.set_callback(on_message)         # Attach the CALLBACK routine
client.subscribe('ae_iot/vasu/temp')    # Hook up to a subscribed topic
client.subscribe('ae_iot/vasu/fan')     # Try with wildcards # and +

while True:
    client.check_msg()     # Periodically chack the incoming message
