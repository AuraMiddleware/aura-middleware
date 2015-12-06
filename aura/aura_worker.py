from aura.managers import DeviceManager as dev
from aura.managers import TaskManager as task

def main():
    dev.DeviceManager().work()
    task.TaskManager().work()

if __name__ == "__main__":
    main()