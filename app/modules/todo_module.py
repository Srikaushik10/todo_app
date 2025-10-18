from datetime import date # Importing the 'date' class from Python's built-in 'datetime' module
from typing import List

"""
The Todo class represents a single task entry.

It defines what information each Todo should hold:
- id:        an integer that uniquely identifies the task
- title:     a short name or summary of the task
- description: more details about what needs to be done
- startDate: the date work begins
- endDate:   the target completion date
"""
class Todo:
    """
    These lines are type hints.  They don’t create data yet;
    they simply declare the expected types so IDEs and
    static analyzers can give better feedback.
    """
    id: int
    title: str
    description: str
    startDate : date
    endDate: date

    """
    The __init__ method is the constructor.
    It runs automatically when you create a new Todo
    and stores the values you pass in on the object itself.
    """
    def __init__(self, id : int, title: str, description:str,startDate:date, endDate:date):
        
        """
        self refers to the specific Todo instance being created.
        Each attribute on self becomes unique to that instance.
        """
        self.id = id
        self.title = title
        self.description = description
        self.startDate = startDate
        self.endDate = endDate
    


todos: List[Todo] = [
    Todo(1, "Learning Basics FastAPI", "Building Todo application using FastAPI", date(2025, 10, 18),date(2025,10,25)),
    Todo(2,"Leaning Git","Understanding and implementing Git commands in my project", date(2025,10,19),date(2025,10,25))
]