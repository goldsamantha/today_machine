import requests
import json
from lib import secrets
from lib import sample
from lib.todos import Todos
from datetime import date

# for Sync api
from todoist.api import TodoistAPI

# alternative approach
# leaving here for now in case i need this...

def main():
    todo_manager = Todos()
    todo_string = todo_manager.getToDoListString()
    print(todo_string)


def getToDoListString():
    # Not totally sure which technique i need for this
    # so going to leave this here for posterity if i need this
    #useSyncLibrary()
    return getInfoFromRestAPI()

def getInfoFromRestAPI():
    today_and_overdue = getRequestData()
    (today_tasks, overdue_tasks) = getTodayAndOverdue(today_and_overdue)
    return getTasksString(today_tasks, overdue_tasks)


def getRequestData():
    return requests.get(
        "https://api.todoist.com/rest/v1/tasks",
        params={
            "filter":  getFilterString()
        },
        headers={
            "Authorization": getHeaderString()
        }
    ).json()


def getFilterString():
    today_date = date.today().isoformat()
    return "(due: %s | overdue)" % today_date

def getHeaderString():
    return "Bearer %s" % secrets.API_TOKEN


def getTasksString(today, overdue):

    s = """
☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ
       Good morning goldsam!
☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ

Here are today's tasks:
"""
    for task in today:
        s += "□ %s\n" % task['content']
    s += "\nHere are your overdue tasks:\n"
    for task in overdue:
        s += "□ %s\n" % task['content']
    
    s += "\n\n\n"

    return s


def getTodayAndOverdue(all_tasks):
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

def useSyncLibrary():
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

main()



