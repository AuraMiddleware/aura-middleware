#!/usr/bin/env python3

from aura.managers import DeviceManager as dev
from aura.managers import TaskManager as task
from zeroless import (Server, Client)

def main():

    device_manager = dev.DeviceManager(12346)
    task_manager = task.TaskManager(port=12347)

    listen_for_push = Server(port=12345).pull()
    for msg in listen_for_push:
        #print(msg.decode())
        device_manager.process(msg.decode())
        #task.TaskManager().work()

if __name__ == "__main__":
    main()