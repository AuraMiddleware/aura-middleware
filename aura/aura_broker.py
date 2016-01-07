#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from aura.managers import helpers
from zeroless import Client, Server

zmq_client = Client()
zmq_client.connect_local(port=helpers.ports['device_manager'])

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

#Listen for gateways' MQTT messages
client.loop_start()

#Listen for DeviceManager ZMQ messages
listen_for_push = Server(port=helpers.ports['broker']).pull()
for msg in listen_for_push:
    client.publish("gateways/broker",msg.decode())

client.loop_stop()