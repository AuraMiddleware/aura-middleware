from eve import Eve
from aura.managers.SemanticManager import serialise

app = Eve()
'''
@app.route('/graph')
def get_graph():
    return serialise()'''

if __name__ == '__main__':
    app.run()
