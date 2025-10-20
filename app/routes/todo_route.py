# Import the service layer module that contains business logic functions
from app.services import todo_service

# Import the Todo class model (used to describe a todo item)
from app.modules.todo_module import Todo, todos

# Import FastAPI classes:
# APIRouter → lets you define route groups that can be attached to your main app
# HTTPException → used to raise custom error responses
from fastapi import APIRouter, HTTPException

# Import type hints for readability and validation
from typing import List, Optional

# Create an APIRouter instance.
# This allows you to register all “/todos” endpoints here
# and later include them into the main FastAPI app.
router = APIRouter()


# --------------------------------------------------------
# GET /todos/
# Endpoint to retrieve all todo items
# --------------------------------------------------------
@router.get("/", response_model=None)
def get_all_todos() -> List[Todo]:
    """
    Fetch all todo items from the service layer.

    Returns:
        A list of todo dictionaries that FastAPI can serialize to JSON.
    """
    # todo_service.get_all_todos() returns a list of Todo objects.
    # vars(todo) converts each Todo object into a dictionary
    # so it can be safely returned as JSON.
    return [vars(todo) for todo in todo_service.get_all_todos()]


# --------------------------------------------------------
# GET /todos/{id}
# Endpoint to retrieve a single todo item by its ID
# --------------------------------------------------------
@router.get("/{id}", response_model=None)
def get_todo_by_id(id: int) -> Optional[Todo]:
    """
    Fetch a single todo by its unique ID.

    Args:
        id (int): The ID of the todo item.

    Returns:
        The todo item as a dictionary if found, or None if not found.
    """
    # Call the service function to get the todo with the given ID
    todo = todo_service.get_todo_by_id(id)

    # If a todo is found, return it as a dictionary
    if todo:
        return vars(todo)

    # If no todo matches the ID, return None.
    # (You could alternatively raise an HTTPException here for clarity.)
    return None


# --------------------------------------------------------------
# POST /todos
# Endpoint to post a todo item
# --------------------------------------------------------------

@router.post("/", response_model=None)
def create_todo(todo: dict):
    """
    Create a new todo item and add it to the in-memory list.
    """
    create_obj = Todo(**todo)
    # Pass the incoming todo object to the service layer
    created_todo = todo_service.create_todo(create_obj)
    return vars(created_todo)


@router.delete("/{id}",response_model=None)
def delete_todo_by_id(id:int):
    deleted_by_id = todo_service.delete_todo_by_id(id)
    return vars(deleted_by_id)