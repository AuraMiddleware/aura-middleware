from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['aura']

collections = ['measurements','devices','platforms','continuous_sensors'
               'discrete_sensors', 'continuous_actuators',
               'discrete_actuators', 'units', 'variables']

def get(collection, document_id):
    result = db[collection].find_one({"@id":document_id})
    return result

def store(collection, document):
    db[collection].insert(document)
    
def remove_id(collection, document_id):
    db[collection].remove({"@id":document_id})
    
def update(collection, document_id, new_document):
    print("update")
