class TaskManager:
    #Assign ZMQ port
    def __init__(self, port):
        print("task_manager called")
        self.port = port
        
    def process(self, input):
        self.task = input
    
    def create_condition(self):
        print("create_condition")
        #TaskManager -> StorageManager
        
    def update_condition(self):
        #TaskManager -> StorageManager
        print("update_condition")
        
    def remove_condition(self):
        #TaskManager -> StorageManager
        print("remove_condition")
        
    def send_command(self, device, command):
        #TaskManager -> DeviceManager
        print("send_command")
        
    def show_tasks(self):
        #TaskManager -> SPARQL
        print("show_tasks")
        
