###########################################
# Ex.1: WiFi Connection
# Ag Instrumentation & IoT Class
# Dept. of Agricultural Engineering, KMITL 
###########################################

import network
import time

SSID = 'Wokwi-GUEST'             # Default Wokwi SSID
PASS = ''

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)   # Create a WiFi Station Interface
wlan.active(True)                     # Activate the interface

wlan.connect(SSID, PASS)              # Ask for a Connection
print('WiFi ', end='')

while not wlan.isconnected():         # Wait for Connection
  print('.', end='')
  time.sleep(0.5)

print(' connected to', wlan.ifconfig()[0]) # Print the IP Address
