from lib.todo_manager import TodoManager
# uncomment to try on the rasp pi
# from lib.hardware_interface import HardwareInterface

def main():
    todo_manager = TodoManager()
    todo_string = todo_manager.getToDoListString()
    print(todo_string)

main()



