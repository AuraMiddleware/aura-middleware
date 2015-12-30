from aura.managers import StorageManager as db

class  DeviceManager:
    
    #Assign ZMQ port
    def __init__(self, port):
        print("DeviceManager running. Port " + str(port))
        self.port = port
    
    def process(self, msg):
        self.msg = msg
        print(self.msg)
    
    def create_device(device):
        db.store('devices',device)

    def update_device(device_id, new_device):
        #DeviceManager -> StorageManager
        db.update('devices', device_id, new_device)

    def remove_device(device_id):
        #DeviceManager -> StorageManager
        db.remove('devices',device_id)
    
    def send_command(command):
        #DeviceManager -> Gateway
        print("sned_command")

    def verify_conditions(measurement):
        #DeviceManager -> SPARQL
        print("verify conditions")