import requests
import json
from datetime import date
from typing import Dict, Tuple, Sequence

from . import secrets

# for Sync api
# alternative approach
# leaving here for now in case i need this...
from todoist.api import TodoistAPI

PREFIX_STRING = """
☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ
    Good morning goldsam!
☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ

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
        (today_tasks, overdue_tasks) = self.getTodayAndOverdue(today_and_overdue)
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


    def getFilterString(self) -> str:
        today_date = date.today().isoformat()
        return "(due: %s | overdue)" % today_date

    def getHeaderString(self) -> str:
        return "Bearer %s" % secrets.API_TOKEN

    def getTasksString(self, today, overdue) -> str:

        s = PREFIX_STRING
        for task in today:
            s += "□ %s\n" % task['content']
        s += "\nHere are your overdue tasks:\n"
        for task in overdue:
            s += "□ %s\n" % task['content']
        
        s += "\n\n\n"

        return s


    def getTodayAndOverdue(self, all_tasks) -> Tuple:
        today = []
        overdue = []
        today_date = date.today().isoformat()

        for task in all_tasks:
            due_date = task['due']['date']
            if (due_date == today_date):
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
