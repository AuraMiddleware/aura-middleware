from aura.managers import StorageManager as db
from zeroless import (Client, Server)
import json

class DeviceManager:
    
    #Assign ZMQ port
    def __init__(self, port):
        print("DeviceManager is running on port " + str(port))
        self.port = port
        self.zmq_client = Client()
        self.zmq_client.connect_local(port=12349)
        self.push = self.zmq_client.push()
    
    def create(self, collection, obj):
        db.store(collection, obj)

    def notify_unknown_object(self, obj_type, obj_id):
        obj = {}
        obj['id'] = obj_id
        obj['type'] = obj_type
        self.push(json.dumps(obj).encode())
    
    def send_command(self, gateway, command):
        #DeviceManager -> Gateway
        print("send_command")
        
    def verify(self, collection, obj_id):
        return (db.get(collection, obj_id) != None)

    def verify_conditions(self, measurement):
        #DeviceManager -> SemanticManager
        print("verify conditions")
        
    def process(self, obj):
        #Measurement
        if obj['@type'] == 'Measurement':
            if self.verify('devices', obj['dev:wasMeasuredBy']):
                self.create('measurements', obj)
                self.verify_conditions(obj)
            else:
                self.notify_unknown_object('Device')
        #Device
        elif obj['@type'] == 'Device':
            if self.verify('platforms', obj['dev:hasPlatform']):
                self.create('devices', obj)
            else:
                self.notify_unknown_object('Platform',obj['dev:hasPlatform'])
        #Platform
        elif obj['@type'] == 'Platform':
            if self.verify('sensors', obj['dev:hasSensor']):
                if self.verify('actuators',obj['dev:hasActuator']):
                    self.create('platforms', obj)
                else:
                    self.notify_unknown_object('Actuator',
                                               obj['dev:hasActuator'])
            else:
                self.notify_unknown_object('Sensor', obj['dev:hasSensor'])
        #ContinuousSensor
        elif obj['@type'] == 'ContinuousSensor':
            if self.verify('units', obj['sense:canMeasure']):
                self.create('sensors', obj)
            else:
                self.notify_unknown_object('Unit', obj['sense:canMeasure'])
        #DiscreteSensor
        elif obj['@type'] == 'DiscreteSensor':
            if self.verify('variables', obj['sense:canMeasure']):
                self.create('sensors', obj)
            else:
                self.notify_unknown_object('Variable', obj['sense:canMeasure'])
        #ContinuousActuator
        elif obj['@type'] == 'ContinuousActuator':
            if self.verify('variables', obj['actuator:increases']):
                self.create('actuators', obj)
            else:
                self.notify_unknown_object('Variable',
                                           obj['actuator:increases'])
        #DiscreteActuator
        elif obj['@type'] == 'DiscreteActuator':
            if self.verify('variables', obj['actuator:changeState']):
                self.create('actuators', obj)
            else:
                self.notify_unknown_object('Variable',
                                           obj['actuator:changeState'])
        #Unit
        elif obj['@type'] == 'Unit':
            if self.verify('variables', obj['sense:unitOf']):
                self.create('units', obj)
            else:
                self.notify_unknown_object('Variable')
        #Variable
        elif obj['@type'] == 'Variable':
            self.create('variables', obj)