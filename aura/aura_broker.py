#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from time import sleep
from zeroless import Client

zmq_client = Client()
zmq_client.connect_local(port=12345)

class AuraBroker():
    def work(self):
        print("AuraBroker called")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gateways/test")

def on_message(client, userdata, msg):
    push = zmq_client.push()
    push(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1885, 60)
client.publish("gateways/broker", "hi")

client.loop_start()

while True:
    sleep(5)
    client.publish("gateways/broker", "i'm the AuraBroker, just checking")