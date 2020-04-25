from datetime import date
from typing import Dict, Tuple, Sequence
import time

TODOIST_TIME_FORMAT_STRING = "%Y-%m-%dT%H:%M:%S%z"

class TodoItem:

    def __init__(self, json_data):
        self.content = json_data['content']
        self.due = json_data['due']
        self.due_date = self.formatDueDate()
        self.due_time = self.formatDueTime()

    def __repr__(self):
        return repr(self.due_time, self.due_date)

    def __str__(self):
        due_time = self.getDueTime()
        due_time_string = ""
        if (due_time):
          due_time_string = time.strftime("%I:%M", due_time) + " -"
        
        return "%s [ ] %s\n" % (due_time_string, self.getContent())

    def getContent(self) -> str:
        return self.content

    def isToday(self) -> bool:
        return self.getDueDate() == date.today()

    def formatDueDate(self) -> date:
        # TODO: should probably make this a datetime object...
        return date.fromisoformat(self.due['date'])

    def getDueDate(self) -> date:
        return self.due_date

    def formatDueTime(self):
        # TODO set this to be an actual time object
        # TODO should check to see if already set, if so return set
        if 'datetime' in self.due:
            time_string = self.due['datetime']
            return time.strptime(time_string, TODOIST_TIME_FORMAT_STRING)
        
        return None

    def getDueTime(self):
        return self.due_time


if __name__ == '__main__':
    print("TodoItem")