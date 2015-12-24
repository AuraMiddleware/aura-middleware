#!/usr/bin/env python3

from aura.managers import DeviceManager as dev
from aura.managers import TaskManager as task
from zeroless import (Server, Client)

def main():
    dev.DeviceManager().work()
    task.TaskManager().work()

if __name__ == "__main__":
    main()