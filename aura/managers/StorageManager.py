from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['aura']

#TODO: Maybe Enum these collection names
devices = db['devices']
platforms = db['platforms']
sense = db['sense']
actuators = db['actuators']
units = db['units']
varialbes = db['variables']
measurements = db['measurements']
conditions = db['conditions']
commands = db['commands']

def get(collection, document_id):
    print("get")

def store(collection, document):
    print("store")
    
def remove_id(collection, document):
    print("remove")
    
def update(collection, document_id, new_document):
    print("update")
