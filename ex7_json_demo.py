# Example 7: JSON Demo

import ujson
from time import sleep_ms

a=0
b=100

while True:
    message = ujson.dumps({
        'sensor1': a,
        'sensor2': b
    })
    print(message)
    a=a+1
    b=b-1
    sleep_ms(3000)