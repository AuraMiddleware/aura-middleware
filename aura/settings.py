MONGO_DBNAME = 'aura'
HATEOAS = False

ITEM_METHODS = ['GET', 'PUT', 'DELETE']
ID_FIELD = '_id'
ITEM_LOOKUP_FIELD = ID_FIELD

additional_lookup = {
            'url': 'regex("[\w]+")',
            'field': 'id',
        }

id = {'type':'string'}

DOMAIN = {
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
    }
}