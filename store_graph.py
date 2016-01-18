from aura.managers import SemanticManager

graph = SemanticManager.get_graph()
if graph != None:
    file = open('graph.xml', 'w')
    file.write(graph.serialize(format='pretty-xml').decode())
    file.close()