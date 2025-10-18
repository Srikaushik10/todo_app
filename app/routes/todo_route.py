from app.services import todo_service
from app.modules.todo_module import Todo
from fastapi import APIRouter, HTTPException
from typing import List, Optional

router = APIRouter()

@router.get("/", response_model=None)
def get_all_todos() -> List[Todo]:
    return [vars(todo) for todo in todo_service.get_all_todos()]

@router.get("/{id}",response_model=None)
def get_todo_by_id(id:int)-> Optional[Todo]:
    todo = todo_service.get_todo_by_id(id)
    if todo:
       return vars(todo)
    return None
