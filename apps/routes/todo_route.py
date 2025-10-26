from apps.services import todo_service
from apps.modules.todo_module import Todo
from fastapi import APIRouter, HTTPException
from typing import List, Optional

router = APIRouter()

# ------------------------------------------------------------
# GET /todos  → get all todos
# ------------------------------------------------------------
@router.get("/", response_model=None)
def get_all_todos() -> List[Todo]:
    """
    Return all todo items as a list of dictionaries.
    """
    return todo_service.get_all_todos()


# ------------------------------------------------------------
# GET /todos/{id}  → get single todo by ID
# ------------------------------------------------------------
@router.get("/{id}", response_model=None)
def get_todo_by_id(id: int) -> Optional[dict]:
    """
    Fetch a single todo by its ID.
    """
    todo = todo_service.get_todo_by_id(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return vars(todo)


# ------------------------------------------------------------
# POST /todos  → create new todo
# ------------------------------------------------------------
@router.post("/", response_model=None)
def add_todo(todo: Todo):
    """
    Create a new todo using plain dictionary input.
    """
    todo_added = todo_service.add_todo(todo)
    return vars(todo_added)


# ------------------------------------------------------------
# PUT /todos/{id}  → update existing todo
# ------------------------------------------------------------
@router.put("/{id}", response_model=None)
def update_todo(id: int, todo: Todo):
    """
    Update a todo by its ID with plain dictionary input.
    """
    updated_todo = todo_service.update_todo(id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return vars(updated_todo)


# ------------------------------------------------------------
# DELETE /todos/{id}  → delete todo by ID
# ------------------------------------------------------------
@router.delete("/{id}", response_model=None)
def delete_todo_by_id(id: int):
    """
    Delete a todo by its ID.
    """
    deleted_todo = todo_service.delete_todo_by_id(id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": f"Todo with ID {id} deleted successfully."}
