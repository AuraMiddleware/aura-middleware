from aura.managers import StorageManager as db

class DeviceManager:
    
    #Assign ZMQ port
    def __init__(self, port):
        print("DeviceManager running. Port " + str(port))
        self.port = port
    
    def create_measurement(self, measurement):
        print("create_measurement")
    
    def create_device(self, device):
        db.store('devices', device)
        
    def create_platform(self, platform):
        db.store('platforms', platform)

    def create_sensor(self, sensor):
        db.store('sensors', sensor)
        
    def create_actuator(aself, actuator):
        db.store('actuators', actuator)
        
    def create_unit(self, unit):
        db.store('units', unit)
        
    def create_variable(self, variable):
        db.store('variables', variable)
        
    def notify_unknown_actuator(self):
        print("notify_unknown_actuator")
    
    def notify_unknown_device(self):
        print("notify_unknown_device")
        
    def notify_unknown_platform(self):
        print("notify_unknown_platform")
    
    def notify_unknown_sensor(self):
        print("notify_unknown_sensor")
    
    def notify_unknown_unit(self):
        print("notify_unknown_unit")
    
    def notify_unknown_variable(self):
        print("notify_unknown_variable")
    
    def send_command(self, command):
        #DeviceManager -> Gateway
        print("send_command")
        
    def verify(self, binding_object):
        print("verify" + str(binding_object))
        return True

    def verify_conditions(self, measurement):
        #DeviceManager -> SPARQL
        print("verify conditions")
        
    def process(self, obj):
        #Measurement
        if obj['@type'] == 'Measurement':
            if self.verify(obj['dev:wasMeasuredBy']):
                self.create_measurement(obj)
                self.verify_conditions(obj)
            else:
                self.notify_unknown_device()
        #Device
        elif obj['@type'] == 'Device':
            if self.verify(obj['dev:hasPlatform']):
                self.create_device(obj)
            else:
                self.notify_unknown_platform()
        #Platform
        elif obj['@type'] == 'Platform':
            if self.verify(obj['dev:hasSensor']):
                if self.verify(obj['dev:hasActuator']):
                    self.create_platform(obj)
                else:
                    self.notify_unknown_actuator()
            else:
                self.notify_unknown_sensor()
        #Sensor
        elif obj['@type'] == 'ContinuousSensor':
            if self.verify(obj['sense:canMeasure']):
                self.create_sensor(obj)
            else:
                self.notify_unknown_unit()
        elif obj['@type'] == 'DiscreteSensor':
            if self.verify(obj['sense:canMeasure']):
                self.create_sensor(obj)
            else:
                self.notify_unknown_variable()
        #Actuator
        elif obj['@type'] in ['ContinuousActuator','DiscreteActuator']:
            if (verify(obj['actuator:increases']) or \
                    self.verify(obj['actuator:changeState'])):
                self.create_actuator(obj)
            else:
                self.notify_unknown_variable()
        #Unit
        elif obj['@type'] == 'Unit':
            if self.verify(obj['sense:unitOf']):
                self.create_unit(obj)
            else:
                self.notify_unknown_variable()
        #Variable
        elif obj['@type'] == 'Variable':
            self.create_variable(obj)