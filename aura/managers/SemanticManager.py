from rdflib import Graph, plugin
from rdflib.store import Store
from rdflib.plugins.sparql import prepareQuery
from aura.managers import StorageManager as db


store = plugin.get('IOMemory', Store)()

def get_graph():
    _graph = Graph(store)
    stored_graph = db.get('graph','graph','id')
    if stored_graph != None:
        _graph.parse(data=stored_graph['graph'].decode(),format='xml')
    return _graph

def make_query(query_string):
    return prepareQuery(query_string)


def query(query_string, bindings=None):
    _graph = get_graph()
    return _graph.query(query_string, initBindings=bindings)


def parse(data_string):
    _graph = get_graph()
    _graph.parse(data=data_string, format='json-ld')
    db.update('graph','graph',{'id':'graph',
                               'graph':_graph.serialize(format='pretty-xml')})


def remove(id):
    _graph = get_graph()
    _graph.remove((id, None, None))
    _graph.remove((None, None, id))
