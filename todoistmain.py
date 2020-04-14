import requests
from lib import secrets

# alternative approach
# leaving here for now in case i need this...
#from todoist.api import TodoistAPI
#api = TodoistAPI(token)
#api.sync()
#print(api.state['projects'])

def main():

    today = requests.get(
        "https://api.todoist.com/rest/v1/tasks",
        params={
        "filter": "(today|overdue)"
        },
        headers={
            "Authorization": "Bearer %s" % secrets.API_TOKEN
        }).json()

    print(today)

main()



