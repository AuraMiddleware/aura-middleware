#!/usr/bin/env python3

from aura.managers import DeviceManager as dev
from aura.managers import TaskManager as task
from zeroless import (Server, Client)
import json

def main():
    device_manager = dev.DeviceManager(12346)
    task_manager = task.TaskManager(12347)

    listen_for_push = Server(port=12345).pull()
    for msg in listen_for_push:
        obj = json.loads(msg.decode())
        if obj['@type'] in ['Device','Measurement','Platform']:
            device_manager.process(obj)
        else:
            print("this type of msg is for TaskManager to process!")
            #task.TaskManager().work()

if __name__ == "__main__":
    main()