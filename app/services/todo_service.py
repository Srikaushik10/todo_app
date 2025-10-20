from app.modules.todo_module import Todo, todos
from typing import List, Optional


# ---------------------------------------------------------
# FUNCTION: get_all_todos
# ---------------------------------------------------------
def get_all_todos() -> List[Todo]:
    """
    Return all todos from the in-memory list.
    """
    return todos


# ---------------------------------------------------------
# FUNCTION: get_todo_by_id
# ---------------------------------------------------------
def get_todo_by_id(id: int) -> Optional[Todo]:
    """
    Return a single todo item by its ID.
    """
    for todo in todos:
        if todo.id == id:
            return todo
    return None


# ---------------------------------------------------------
# FUNCTION: create_todo
# ---------------------------------------------------------
def create_todo(todo: Todo) -> Todo:
    """
    Add a new todo to the list.
    Automatically generates an incremental ID.
    """
    # Auto-generate ID
    if todos:
        todo.id = todos[-1].id + 1
    else:
        todo.id = 1

    todos.append(todo)
    return todo


# ---------------------------------------------------------
# FUNCTION: update_todo
# ---------------------------------------------------------
def update_todo(id: int, todo: Todo) -> Optional[Todo]:
    """
    Update an existing todo by its ID.
    If found, replace it and return the updated item.
    """
    for i, existing_todo in enumerate(todos):
        if existing_todo.id == id:
            todo.id = id  # keep same ID
            todos[i] = todo
            return todos[i]
    return None


# ---------------------------------------------------------
# FUNCTION: delete_todo_by_id
# ---------------------------------------------------------
def delete_todo_by_id(id: int) -> Optional[Todo]:
    """
    Delete a todo by its ID and return the deleted object.
    """
    for index, todo in enumerate(todos):
        if todo.id == id:
            deleted_todo = todos.pop(index)
            return deleted_todo
    return None
