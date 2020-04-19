from lib.todo_manager import TodoManager
# uncomment to try on the rasp pi
from lib.hardware_interface import HardwareInterface
from time import sleep

def main():
    todo_manager = TodoManager()
    print("todo manager instantiated...")
    h = HardwareInterface()
    print("hardware instantiated...")
    while True:
        if (h.isButtonPressed()):
            print("button pressed!\n")
            todo_string = todo_manager.getToDoListString()
            h.writeToPrinter(todo_string)
        sleep(.5)


main()



