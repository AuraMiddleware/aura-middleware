from pymongo import MongoClient

client = MongoClient('localhost', 27017)

#TODO delete it later
client.drop_database('aura')

db = client['aura']

#TODO: Maybe Enum these collection names
devices = db['devices']
platforms = db['platforms']
continuous_sensors = db['continuous_sensors']
discrete_sensors = db['discrete_sensors']
continuous_actuators = db['continuous_actuators']
discrete_actuators = db['discrete_actuators']
units = db['units']
variables = db['variables']
measurements = db['measurements']
conditions = db['conditions']
commands = db['commands']

def get(collection, document_id):
    result = db[collection].find_one({"@id":document_id})
    print("get("+collection+","+document_id+"):\n" + str(result) + "\n")
    return result

def store(collection, document):
    db[collection].insert(document)
    get(collection, document["@id"])
    
def remove_id(collection, document_id):
    db[collection].remove({"@id":document_id})
    
def update(collection, document_id, new_document):
    print("update")
