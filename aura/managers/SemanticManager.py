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


def update_graph(graph):
    db.update('graph','graph',
              {'id':'graph','graph':graph.serialize(format='pretty-xml')})


def make_query(query_string, namespaces=None):
    return prepareQuery(query_string, initNs=namespaces)


def query(query_string, bindings=None):
    _graph = get_graph()
    result = _graph.query(query_string, initBindings=bindings)
    return result

def parse(data_string):
    _graph = get_graph()
    _graph.parse(data=data_string, format='json-ld')
    update_graph(_graph)


def remove(id):
    _graph = get_graph()
    _graph.remove((id, None, None))
    _graph.remove((None, None, id))
    update_graph(_graph)
