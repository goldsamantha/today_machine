import requests
import json
from lib import secrets
from lib import sample
from lib.todo_manager import TodoManager
from datetime import date

# for Sync api
from todoist.api import TodoistAPI

# alternative approach
# leaving here for now in case i need this...

def main():
    todo_manager = TodoManager()
    todo_string = todo_manager.getToDoListString()
    print(todo_string)



main()



