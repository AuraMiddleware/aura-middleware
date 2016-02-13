from eve import Eve
from aura.managers import SemanticManager as graph
from aura.managers import TaskManager as task
import json

def parse(items):
    item = items[0]
    obj = {}
    for key in item:
        if key in ["id","@context","@type","id","minValue","maxValue",
                   "task:enforces", "value"]:
            obj[key] = item[key]
    graph.parse(json.dumps(obj))


def remove(items):
    for i in items:
        graph.remove(items[i]['id'])


app = Eve()


@app.route('/commands/possibilities')
def get_possible_commands():
    response = task.get_available_commands()
    return json.dumps(response)


@app.route('/conditions/possibilities')
def get_possible_conditions():
    response = task.get_available_conditions()
    return json.dumps(response)


app.on_insert_commands += parse
app.on_insert_conditions += parse
app.on_delete_commands += remove
app.on_delete_conditions += remove


if __name__ == '__main__':
    app.run()
