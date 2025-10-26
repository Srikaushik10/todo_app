from datetime import date # Importing the 'date' class from Python's built-in 'datetime' module
from typing import List
from pydantic import BaseModel

class Todo(BaseModel):
    id : int
    title: str
    description : str
    startDate: date
    endDate: date


# todos: List[Todo] = [
#     Todo(1, "Learning Basics FastAPI", "Building Todo application using FastAPI", date(2025, 10, 20), date(2025, 10, 25)),
#     Todo(2, "Learn Git", "Understand branching and merging", date(2025, 10, 21), date(2025, 10, 22))
# ]

todos: List[Todo] = [
    Todo(id= 1, title= "Learning Basics FastAPI", description= "Building Todo application using FastAPI", startDate= date(2025, 10, 18), endDate= date(2025,10,25)),
    Todo(id= 2, title= "Leaning Git", description= "Understanding and implementing Git commands in my project", startDate= date(2025,10,19), endDate= date(2025,10,25)),
    Todo(id= 3, title= "Practicing AWS Bedrock", description= "Understanding the ChatBots using AWS Bedrock", startDate= date(2025,10,21), endDate= date(2025,10,31))
]
