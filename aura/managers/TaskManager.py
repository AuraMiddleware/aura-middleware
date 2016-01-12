from zeroless import (Client, Server)
import json

from aura.managers import SemanticGraph as graph
from aura.managers import StorageManager as db
from aura.managers import helpers

zmq_device = Client()
zmq_device.connect_local(port=helpers.ports['device_manager'])
push_to_device = zmq_device.push()
    
def create_condition(condition):
    print("create_condition")
    #TaskManager -> StorageManager
    db.store('conditions', condition)

def update_condition():
    #TaskManager -> StorageManager
    print("update_condition")

def remove_condition():
    #TaskManager -> StorageManager
    print("remove_condition")

def send_command(device, command):
    #TaskManager -> DeviceManager
    print("send_command")

def test_conditions(measurement):
    print("testing conditions")

def get_available_tasks():
    #TaskManager -> SemanticManager
    print("show_tasks")

listen_for_push = Server(port=helpers.ports['task_manager']).pull()
for msg in listen_for_push:
    obj = json.loads(msg.decode())
    if obj['@type'] == 'Measurement':
        test_conditions(obj)
    else:
        print("i don't know what to do with this message")
