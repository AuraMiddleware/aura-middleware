from eve import Eve
from aura.managers import SemanticManager as graph
from aura.managers import StorageManager as db
import json

def parse(items):
    item = items[0]
    obj = {}
    for key in item:
        if key in ["id","@context","@type","id","minValue","maxValue",
                   "task:enforces", "value"]:
            obj[key] = item[key]
    graph.parse(json.dumps(obj))


app = Eve()

app.on_insert_commands += parse
app.on_insert_conditions += parse

if __name__ == '__main__':
    app.run()
