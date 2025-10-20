# Import the Todo class and the in-memory todos list from the module layer.
# Todo → defines the structure of a single todo item.
# todos → acts as a mock database (list of Todo objects).
from app.modules.todo_module import Todo, todos

# Import List and Optional for type hints.
# List[Todo] means the function returns a list of Todo objects.
# Optional[Todo] means the function can return either a Todo object or None.
from typing import List, Optional


"""
This file represents the SERVICE LAYER of the application.

The service layer contains the application's BUSINESS LOGIC.
It sits between the API routes and the data (in-memory list or database).

Currently, it works with static in-memory data (the 'todos' list),
but later you can easily replace this logic with a database layer (e.g., SQLAlchemy or MongoDB)
without changing your route handlers.
"""


# ---------------------------------------------------------
# FUNCTION: get_all_todos
# ---------------------------------------------------------
def get_all_todos() -> List[Todo]:
    """
    Fetch and return all todo items from the data source.

    Returns:
        List[Todo]: A list containing all Todo objects currently stored
        in the in-memory data list ('todos').
    """
    # 'todos' is a list imported from todo_module that holds all Todo objects.
    # Since this is static data for now, we simply return it directly.
    return todos


# ---------------------------------------------------------
# FUNCTION: get_todo_by_id
# ---------------------------------------------------------
def get_todo_by_id(id: int) -> Optional[Todo]:
    """
    Find and return a specific todo item by its unique ID.

    Args:
        id (int): The unique identifier of the todo item to search for.

    Returns:
        Optional[Todo]: The Todo object if found; otherwise, None.
    """
    # Loop through the list of todos to find a match by ID.
    for todo in todos:
        # Check if the current todo object's ID matches the requested one.
        if todo.id == id:
            # Return the matching todo object if found.
            return todo

    # If no todo matches the given ID, return None.
    # This indicates to the API layer that the todo wasn't found.
    return None


# ---------------------------------------------------------
# FUNCTION: get_todo_by_id
# ---------------------------------------------------------
def create_todo(todo: Todo) -> Optional[Todo]:
    """
    Add a new todo item to the in-memory data list.
    
    Args:
        todo (Todo): The new todo item sent from the client.
    
    Returns:
        Todo: The newly created todo item.
    """
    todos.append(todo)
    return todo


# ---------------------------------------------------------
# FUNCTION: delete_todo_by_id
# ---------------------------------------------------------
def delete_todo_by_id(id:int) -> Optional[Todo]:
    for index, todo in enumerate(todos):
        if todo.id == id:
                deleted_todo = todos.pop(index)
                return deleted_todo
    return None       
   