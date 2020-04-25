from datetime import date
from typing import Dict, Tuple, Sequence
import time

TODOIST_TIME_FORMAT_STRING = "%Y-%m-%dT%H:%M:%S%z"

class TodoItem:

    def __init__(self, json_data):
        self.content = json_data['content']
        self.due = json_data['due']

    def getContent(self) -> str:
        return self.content

    def isToday(self) -> bool:
        return self.getDueDate() == date.today()
    
    def getDueDate(self):
        # TODO: should probably make this a datetime object...
        return date.fromisoformat(self.due['date'])
    
    def getDueTime(self):
        # TODO set this to be an actual time object
        # TODO should check to see if already set, if so return set
        if 'datetime' in self.due:
            time_string = self.due['datetime']
            return time.strptime(time_string, TODOIST_TIME_FORMAT_STRING)
        
        return None


if __name__ == '__main__':
    print("TodoItem")