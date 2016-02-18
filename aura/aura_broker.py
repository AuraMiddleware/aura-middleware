#!/usr/bin/env python3

import argparse
import paho.mqtt.client as mqtt
from aura.managers import helpers
from zeroless import Client, Server


zmq_client = Client()
zmq_client.connect_local(port=helpers.ports['device_manager'])
zmq_push = zmq_client.push()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gateways/test")


def on_message(client, userdata, msg):
    zmq_push(msg.payload)


#Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("mqtt_broker_ip")
parser.add_argument("mqtt_port", type=int)
args = parser.parse_args()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(args.mqtt_broker_ip, args.mqtt_port, 60)

#Listen for gateways' MQTT messages
client.loop_start()

#Listen for DeviceManager ZMQ messages
listen_for_push = Server(port=helpers.ports['broker']).pull()
for msg in listen_for_push:
    print(msg.decode())
    client.publish("gateways/broker",msg.decode())

client.loop_stop()