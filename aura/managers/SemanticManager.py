from rdflib import Graph, ConjunctiveGraph
from rdflib import plugin
from rdflib.store import Store
from aura.managers import StorageManager as db

store = plugin.get('IOMemory', Store)()
_local = Graph(store)
_graph = ConjunctiveGraph(store)


def query(query_string, binding=None):
    _global = Graph(store)
    _global.parse(data=db.get('graph',"graph","id")["graph"].decode(),
                  format="application/rdf+xml")
    return _global.query(query_string, initBindings=binding)


def serialise():
    _local.parse(data=db.get('graph',"graph","id")["graph"].decode(),
                  format="application/rdf+xml")
    return _local.serialize(format='pretty-xml')


def parse(data_string):
    _local.parse(data=data_string, format='json-ld')
    db.update('graph', "graph", {"id": "graph", "graph": serialise()})


def remove(id):
    _local.remove((id, None, None))
    _local.remove((None, None, id))
