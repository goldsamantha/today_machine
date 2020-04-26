import requests
import json
from datetime import date, datetime
import time
from typing import Dict, Tuple, Sequence, List

from . import secrets
from .todo_item import TodoItem

# for Sync api
# alternative approach
# leaving here for now in case i need this...
from todoist.api import TodoistAPI

PREFIX_STRING = """
*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
      Good morning goldsam!
*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~

Here are today's tasks:
"""

class TodoManager:

    def getToDoListString(self) -> str: 
        # Not totally sure which technique i need for this
        # so going to leave this here for posterity if i need this
        #useSyncLibrary()
        return self.getInfoFromRestAPI()

    def getInfoFromRestAPI(self) -> str:
        today_and_overdue = self.getRequestData()

        # TODO: should probably do this setting in the constructor instead
        self.task_objects = self.formatTaskObjects(today_and_overdue)
        (today_tasks, overdue_tasks) = self.getTodayAndOverdue(self.task_objects) #today_and_overdue)
        return self.getTasksString(today_tasks, overdue_tasks)


    def getRequestData(self):
        return requests.get(
            "https://api.todoist.com/rest/v1/tasks",
            params={
                "filter":  self.getFilterString()
            },
            headers={
                "Authorization": self.getHeaderString()
            }
        ).json()

    def formatTaskObjects(self, task_data) -> List[TodoItem]:
        tasks = [TodoItem(item) for item in task_data]

        # TODO - this is maybe stupid--should def write tests for this
        late_st = time.strptime("23:59", "%H:%M")
        late = datetime.fromtimestamp(time.mktime(late_st))
        tasks.sort(key=lambda item: item.getDueTime().time() if item.getDueTime() != None else late.time())
        return tasks

    def getTaskObjects(self) -> List[TodoItem]:
        return self.task_objects

    def getFilterString(self) -> str:
        today_date = date.today().isoformat()
        return "(due: %s | overdue)" % today_date

    def getHeaderString(self) -> str:
        return "Bearer %s" % secrets.API_TOKEN

    def getTasksString(self, today: List[TodoItem], overdue: List[TodoItem]) -> str:

        s = PREFIX_STRING
        for task in today:
            s += str(task)
        s += "\nHere are your overdue tasks:\n"
        for task in overdue:
            s += str(task)

        s += "[ ]\n[ ]\n[ ]\n\n\n\n\n"

        return s

    """
    - Filter out all of the tasks that are for today
    - Filter out all of the tasks WITH timestamps 
    """

    def getTodayAndOverdue(self, all_tasks: List[TodoItem]) -> Tuple:
        today = []
        overdue = []

        for task in all_tasks:
            if (task.isToday()):
                today.append(task)
            else:
                overdue.append(task)

        return (today, overdue)

    def useSyncLibrary(self):
        api = TodoistAPI(secrets.API_TOKEN)
        api.sync()
        #print(api.state['projects'])
        print("\n\n\n")
        items = api.state["items"]
        print(json.dumps(items))

        # get all completed
        all_comp = api.completed.get_all()

        for item in items:
            if item['checked'] > 0:
                print(item['content'])


if __name__ == '__main__':
    print("todo_manager.py")
