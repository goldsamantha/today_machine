from datetime import date, datetime
from typing import Dict, Tuple, Sequence
import time
import pytz

TODOIST_TIME_FORMAT_STRING = "%Y-%m-%dT%H:%M:%S%z"

class TodoItem:

    def __init__(self, json_data):
        self.content = json_data['content']
        self.due = json_data['due']
        self.due_date = self.formatDueDate()
        self.due_time = self.formatDueTime()

    def __repr__(self):
        return repr((self.due_time, self.due_date))

    def __str__(self):
        return "%s[ ] %s\n" % (self.getDueTimeString(), self.getContent())

    def getContent(self) -> str:
        return self.content

    def isToday(self) -> bool:
        return self.getDueDate().date() == date.today()

    def formatDueDate(self) -> datetime:
        # TODO: should probably make this a datetime object...
        return datetime.fromisoformat(self.due['date'])

    def getDueDate(self) -> datetime:
        return self.due_date

    def getDueTimeString(self) -> str:
        due_time = self.getDueTime()

        if (due_time == None):
            return ''
        
        eastern = pytz.timezone('US/Eastern')
        due_time = pytz.utc.localize(due_time)
        return due_time.astimezone(eastern).strftime("%I:%M") + " "

    def formatDueTime(self):
        # TODO should check to see if already set, if so return set
        if 'datetime' in self.due:
            time_string = self.due['datetime']
            time_string = time_string[0:-1] # strip off the "Z"

            return datetime.fromisoformat(time_string)
        
        return None

    def getDueTime(self):
        return self.due_time


if __name__ == '__main__':
    print("TodoItem")