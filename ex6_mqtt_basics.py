# Example 6: Simple Pub/Sub Demo on NETPIE

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
wlan.connect(WiFi_SSID,WiFi_PASS)
print('WiFi ', end='')
while not wlan.isconnected():
    print('.', end='')
    sleep_ms(500)
print(' connected to', wlan.ifconfig()[0])

# Connect to MQTT broker
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_TOKEN, password=MQTT_SECRET)
try:
    client.connect()
    print('MQTT Connected')
except:
    print('MQTT Error')

# Callback function for responding to the subscribed topics
def on_message(topic,msg):
    print(topic,':',msg.decode('utf8'))

client.set_callback(on_message)
client.subscribe('@msg/#')

i = 0
while True:
    client.check_msg()
    client.publish('@msg/sensor', str(i))
    i = i+1
    sleep_ms(3000)
