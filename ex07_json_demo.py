# Example 7: JSON Demo

import ujson
import time

a = 0
b = 100

while True:
    msg_dic = {
        'sensor1': a,
        'sensor2': b
    }
    msg_json = ujson.dumps(msg_dic)
    print(msg_dic, msg_json)
    a = a+1
    b = b-1
    time.sleep(3)
