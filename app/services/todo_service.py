from app.modules.todo_module import Todo, todos
from typing import List, Optional

"""
The service layer acts as the logic layer between your API routes and data.
For now, it works with static in-memory data. Later, you can replace it with DB logic.
"""

def get_all_todos() -> List[Todo]:
    """Return all todo items."""
    return todos

def get_todo_by_id(id: int) -> Optional[Todo]:
    """Find a todo by its ID."""
    for todo in todos:
        if todo.id == id:
            return todo
    return None
