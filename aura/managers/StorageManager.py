from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['aura']

collections = ['graph','measurements','devices','platforms',
               'continuous_sensors',
               'discrete_sensors', 'continuous_actuators', 'conditions',
               'discrete_actuators', 'units', 'variables', 'commands']

def get(collection, document_id, key="@id"):
    result = db[collection].find_one({key:document_id})
    return result

def store(collection, document):
    db[collection].insert(document)
    
def remove_id(collection, document_id):
    db[collection].remove({"@id":document_id})
    
def update(collection, document_id, new_document):
    db[collection].find_one_and_replace({"id":document_id}, new_document,
                                        upsert=True)
