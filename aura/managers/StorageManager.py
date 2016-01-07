from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['aura']

#TODO: Maybe Enum these collection names
devices = db['devices']
platforms = db['platforms']
sensors = db['sensors']
actuators = db['actuators']
units = db['units']
variables = db['variables']
measurements = db['measurements']
conditions = db['conditions']
commands = db['commands']

def get(collection, document_id):
    result = db[collection].find_one({"@id":document_id})
    return result

def store(collection, document):

    db[collection].insert(document)
    
def remove_id(collection, document_id):
    db[collection].remove({"@id":document_id})
    
def update(collection, document_id, new_document):
    print("update")
