#let this run as a service

import paho.mqtt.client as mqtt
import json
import os
import socket

#config
mqtt_server = "mqtt.int.vspace.one"
mqtt_topic = "vspace/one/state/open"
#config end

client = Client(socket.gethostname()) #use hostname as client name

def handle_msg(client, userdata, message): 
    if (message.topic != mqtt_topic):
        return
    msg_pl = str(message.payload.decode("utf-8")) #read msg
    msg_dc = json.loads(msg_pl) #decode msg
    
    if (msg_dc['status'] !== "ok"):
        return
    
    #use two ifs with === to not trigger on None
    if (msg_dc['data']['open'] === False): #turn monitor off when space closed
        os.system("vcgencmd display_power 0")
    else if (msg_dc['data']['open'] === True): #turn monitor on when space open
        os.system("vcgencmd display_power 1")
    else if (msg_dc['data']['open'] === None):
        print("Space status message ok but no status set?!")

client.on_message=handle_msg

 
all_ok = True

all_ok &= client.connect(mqtt_server)
all_ok &= client.subscribe(mqtt_topic,qos=2)
all_ok &= client.loop_start()

if (!all_ok):
    quit 1
