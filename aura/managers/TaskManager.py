from zeroless import (Client, Server)
import json
from aura.managers import SemanticManager as graph
from aura.managers import StorageManager as db
from aura.managers import helpers

zmq_device = Client()
zmq_device.connect_local(port=helpers.ports['device_manager'])
push_to_device = zmq_device.push()

def create_condition(condition):
    print("create_condition")
    # TaskManager -> StorageManager
    db.store('conditions', condition)


def update_condition():
    # TaskManager -> StorageManager
    print("update_condition")


def remove_condition():
    # TaskManager -> StorageManager
    print("remove_condition")


def send_command(device, command):
    # TaskManager -> DeviceManager
    print("send_command")


available_conditions = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX auraDevice: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraDevice#>
    PREFIX auraSense: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraSense#>

    SELECT DISTINCT ?device ?variable
    WHERE {
        ?device auraDevice:hasPlatform ?platform .
  		?platform auraDevice:hasSensor ?sensor .
        ?sensor auraSense:canMeasure ?variable .
        ?variable rdf:type auraSense:Variable
    }"""

available_cont_conditions = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX auraDevice: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraDevice#>
    PREFIX auraSense: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraSense#>

    SELECT DISTINCT ?device ?variable ?unit
    WHERE {
        ?device auraDevice:hasPlatform ?platform .
  		?platform auraDevice:hasSensor ?sensor .
        ?sensor auraSense:canMeasure ?unit .
        ?unit auraSense:unitOf ?variable
    }"""


available_commands = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX auraDevice: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraDevice#>
    PREFIX auraActuate: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraActuate#>

    SELECT DISTINCT ?device ?variable
    WHERE {
        ?device auraDevice:hasPlatform ?platform .
  		?platform auraDevice:hasActuator ?actuator .
        ?actuator auraActuate:changeState ?variable.
    }"""

available_cont_commands = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX auraDevice: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraDevice#>
    PREFIX auraActuate: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraActuate#>

    SELECT DISTINCT ?device ?variable
    WHERE {
        ?device auraDevice:hasPlatform ?platform .
  		?platform auraDevice:hasActuator ?actuator .
        ?actuator auraActuate:increases ?variable.
    }"""

conditions_query = graph.make_query(available_conditions)
conditions_cont_query = graph.make_query(available_cont_conditions)
commands_query = graph.make_query(available_commands)
commands_cont_query = graph.make_query(available_cont_commands)


def get_available_conditions():
    discrete_result = graph.query(conditions_query)
    continuous_result = graph.query(conditions_cont_query)
    response = {}
    i = 0
    for row in discrete_result:
        response[i] = {'device':row[0], 'variable':row[1]}
        i += 1
    for row in continuous_result:
        response[i] = {'device':row[0], 'variable':row[1], 'unit':row[2]}
        i += 1

    return response


def get_available_commands():
    discrete_result = graph.query(commands_query)
    continuous_result = graph.query(commands_cont_query)
    response = {}
    i = 0
    for row in discrete_result:
        response[i] = {'device':row[0], 'variable':row[1]}
        i += 1
    for row in continuous_result:
        response[i] = {'device':row[0], 'variable':row[1]}
        i += 1

    return(response)


def trigger_commands(condition):
    print("trigger commands!")
    print(condition)


def test_conditions(measurement):
    measurement_str = measurement["@id"]
    var_str = measurement["dev:valueOf"]

    conditions_str = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX auraTask: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraTask#>
    PREFIX auraDev: <https://raw.githubusercontent.com/viniciusmsfraga/auramiddleware/master/semantics/ontologies/AuraDevice#>
    PREFIX variable: <"""+var_str+""">
    PREFIX measurement: <"""+measurement_str+""">

    SELECT DISTINCT ?condition ?minValue ?maxValue ?value
    WHERE {
        measurement: auraDev:Value ?value .
        ?condition auraTask:enforces variable: .
    	?condition auraTask:Range:MinValue ?minValue .
        ?condition auraTask:Range:MaxValue ?maxValue .
        FILTER(?value < ?minValue || ?value > ?maxValue)
    }
    """

    result = graph.query(conditions_str)
    i = 0
    for row in result:
        i += 1
        print("violated condition #" + str(i))
        print(row[0])#condition?
        print(row[1])#minValue
        print(row[2])#maxValue
        print(row[3])#value


def main():
    listen_for_push = Server(port=helpers.ports['task_manager']).pull()
    for msg in listen_for_push:
        obj = json.loads(msg.decode())
        if obj['@type'] == 'Measurement':
            test_conditions(obj)
        else:
            print("i don't know what to do with this message")

if __name__ == '__main__':
    main()