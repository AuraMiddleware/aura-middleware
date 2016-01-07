from aura.managers import StorageManager as db
from zeroless import (Client, Server)
from aura.managers import helpers
import json

zmq_broker = Client()
zmq_broker.connect_local(port=helpers.ports['broker'])
push_to_broker = zmq_broker.push()

zmq_task = Client()
zmq_task.connect_local(port=helpers.ports['task_manager'])
push_to_task = zmq_task.push()

def verify(collection, obj_id):
    return (db.get(collection, obj_id) != None)

def create(collection, obj):
    if not verify(collection, obj['@id']):
        db.store(collection, obj)
    else:
        print("Already have " + str(obj['@id']) + " in database.")

def notify_unknown_object(obj_type, obj_id):
    obj = {}
    obj['id'] = obj_id
    obj['type'] = obj_type
    push_to_broker(json.dumps(obj).encode())

def send_command(device, command):
    #DeviceManager -> Gateway
    print("send_command")

listen_for_push = Server(port=helpers.ports['device_manager']).pull()
for msg in listen_for_push:
    obj = json.loads(msg.decode())
    #Measurement
    if obj['@type'] == 'Measurement':
        if verify('devices', obj['dev:wasMeasuredBy']):
            create('measurements', obj)
            push_to_task(msg)
        else:
            notify_unknown_object('Device')
    #Device
    elif obj['@type'] == 'Device':
        if verify('platforms', obj['dev:hasPlatform']):
            create('devices', obj)
        else:
            notify_unknown_object('Platform',obj['dev:hasPlatform'])
    #Platform
    elif obj['@type'] == 'Platform':
        if verify('sensors', obj['dev:hasSensor']):
            if verify('actuators',obj['dev:hasActuator']):
                create('platforms', obj)
            else:
                notify_unknown_object('Actuator', obj['dev:hasActuator'])
        else:
            notify_unknown_object('Sensor', obj['dev:hasSensor'])
    #ContinuousSensor
    elif obj['@type'] == 'ContinuousSensor':
        if verify('units', obj['sense:canMeasure']):
            create('sensors', obj)
        else:
            notify_unknown_object('Unit', obj['sense:canMeasure'])
    #DiscreteSensor
    elif obj['@type'] == 'DiscreteSensor':
        if verify('variables', obj['sense:canMeasure']):
            create('sensors', obj)
        else:
            notify_unknown_object('Variable', obj['sense:canMeasure'])
    #ContinuousActuator
    elif obj['@type'] == 'ContinuousActuator':
        if verify('variables', obj['actuator:increases']):
            create('actuators', obj)
        else:
            notify_unknown_object('Variable', obj['actuator:increases'])
    #DiscreteActuator
    elif obj['@type'] == 'DiscreteActuator':
        if verify('variables', obj['actuator:changeState']):
            create('actuators', obj)
        else:
            notify_unknown_object('Variable', obj['actuator:changeState'])
    #Unit
    elif obj['@type'] == 'Unit':
        if verify('variables', obj['sense:unitOf']):
            create('units', obj)
        else:
            notify_unknown_object('Variable', obj['sense:unitOf'])
    #Variable
    elif obj['@type'] == 'Variable':
        create('variables', obj)