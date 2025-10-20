from apps.services import todo_service
from apps.modules.todo_module import Todo
from fastapi import APIRouter, HTTPException
from typing import List, Optional

router = APIRouter()

# ------------------------------------------------------------
# GET /todos  → get all todos
# ------------------------------------------------------------
@router.get("/", response_model=None)
def get_all_todos() -> List[dict]:
    """
    Return all todo items as a list of dictionaries.
    """
    return [vars(todo) for todo in todo_service.get_all_todos()]


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
def create_todo(todo: dict):
    """
    Create a new todo using plain dictionary input.
    """
    # Convert dict → Todo object manually (no Pydantic used)
    create_obj = Todo(
        id=todo.get("id"),
        title=todo.get("title"),
        description=todo.get("description"),
        startDate=todo.get("startDate"),
        endDate=todo.get("endDate"),
    )
    created_todo = todo_service.create_todo(create_obj)
    return vars(created_todo)


# ------------------------------------------------------------
# PUT /todos/{id}  → update existing todo
# ------------------------------------------------------------
@router.put("/{id}", response_model=None)
def update_todo(id: int, todo: dict):
    """
    Update a todo by its ID with plain dictionary input.
    """
    update_obj = Todo(
        id=id,
        title=todo.get("title"),
        description=todo.get("description"),
        startDate=todo.get("startDate"),
        endDate=todo.get("endDate"),
    )
    updated_todo = todo_service.update_todo(id, update_obj)
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
