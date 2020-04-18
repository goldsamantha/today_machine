from lib.todo_manager import TodoManager

def main():
    todo_manager = TodoManager()
    todo_string = todo_manager.getToDoListString()
    print(todo_string)

main()



