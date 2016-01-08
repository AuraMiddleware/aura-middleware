from rdflib import Graph, ConjunctiveGraph
from rdflib import Namespace, plugin
from rdflib.store import Store

from aura.managers import StorageManager as db

store = plugin.get('IOMemory', Store)()
local = Graph(store)
graph = ConjunctiveGraph(store)

def query(query_string, binding=None):
    _global = Graph(store)
    _global.parse("http://localhost:5000/graph",
                  format="application/rdf+xml")
    return graph.query(query_string, initBindings=binding)

def parse(data_string):
    local.parse(data=data_string, format='json-ld')

def serialise():
    return local.serialize(format='pretty-xml')

def remove(id):
    local.remove((id, None, None))
    local.remove((None, None, id))