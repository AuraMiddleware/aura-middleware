#!/usr/bin/env python3

from aura.managers import DeviceManager as dev
from aura.managers import TaskManager as task
from zeroless import (Server, Client)

def main():
    #dev.DeviceManager().work()
    #task.TaskManager().work()

    listen_for_push = Server(port=12345).pull()
    for msg in listen_for_push:
        print(msg.decode())

if __name__ == "__main__":
    main()