MONGO_DBNAME = 'aura'
HATEOAS = False

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PUT', 'DELETE']
ID_FIELD = '_id'
ITEM_LOOKUP_FIELD = ID_FIELD

additional_lookup = {
            'url': 'regex("[\w]+")',
            'field': 'id',
        }

id = {'type':'string'}

DOMAIN = {
    'graph':{
        'schema':{
            "graph":{}
        }
    },
    'devices': {
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            '@id':{},
            '@type':{},
            '@context':{},
            'dev:hasPlatform':{},
        }
    },
    'measurements':{
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@type":{},
            "@id":{},
            "dev:wasMeasuredBy":{},
            "dev:valueOf":{},
            "value":{},
            "timestamp":{}
        }
    },
    'platforms':{
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            '@id':{},
            "@context":{},
            "@type":{},
            "brand":{},
            "dev:hasSensor":{},
            "dev:hasActuator":{}
        }
    },
    'continuous_sensors':{
        'url':'sensors/continuous',
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@type":{},
            "@id":{},
            "sense:canMeasure":{},
            "precision":{},
            "minValue":{},
            "maxValue":{}
        }
    },
    'discrete_sensors':{
        'url':'sensors/discrete',
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@type":{},
            "@id":{},
            "sense:canMeasure":{}
        }
    },
    'continuous_actuators':{
        'url':'actuators/continuous',
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@type":{},
            "@id":{},
            "actuator:increases":{},
            "actuator:decreases":{}
        }
    },
    'discrete_actuators':{
        'url':'actuators/discrete',
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@type":{},
            "@id":{},
            "actuator:changeState":{}
        }
    },
    'units':{
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@id":{},
            "@type":{},
            "sense:unitOf":{}
        }
    },
    'variables':{
        'additional_lookup': additional_lookup,
        'schema':{
            'id':id,
            "@context":{},
            "@id":{},
            "@type":{}
        }
    },
    'commands':{
        'additional_lookup': additional_lookup,
        'schema':{
            "id": id,
            "@context": {},
            "@type": {},
            "@id": {},
            "value": {},
            "task:enforces": {}
        }
    },
    'conditions':{
        'additional_lookup': additional_lookup,
        'schema':{
            "id": id,
            "@context": {},
            "@type": {},
            "@id": {},
            "minValue": {},
            "maxValue": {},
            "task:enforces": {},
            "task:triggers":{}
        }
    },
}