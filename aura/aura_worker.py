#!/usr/bin/env python3

import json

from zeroless import (Server)

from aura.managers import DeviceManager as dev
from aura.managers import TaskManager as task
from aura.managers import helpers

def main():
    device_manager = dev.DeviceManager(helpers.zmq_ports['devices'])
    task_manager = task.TaskManager(helpers.zmq_ports['tasks'])
    device_related = ['Measurement', 'Device', 'Platform',
                      'ContinuousActuator', 'DiscreteActuator',
                      'ContinuousSensor','DiscreteSensor',
                      'Unit', 'Variable']

    listen_for_push = Server(port=12345).pull()
    for msg in listen_for_push:
        obj = json.loads(msg.decode())
        if obj['@type'] in device_related:
            device_manager.process(obj)
        else:
            print("this type of msg is for TaskManager to process!")
            #task_manager.process(obj)

if __name__ == "__main__":
    main()