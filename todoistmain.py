from lib.todo_manager import TodoManager
# uncomment to try on the rasp pi
from lib.hardware_interface import HardwareInterface
from time import sleep

def main():
    todo_manager = TodoManager()
    h = HardwareInterface()
    while True:
        if (h.isButtonPressed()):
            todo_string = todo_manager.getToDoListString()
            h.writeToPrinter(todo_string)
        sleep(.5)


main()



