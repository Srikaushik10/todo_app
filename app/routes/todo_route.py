
from app.services import todo_service 
from app.modules.todo_module import Todo,todos 
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.get("/", response_model=None)
def get_all_todos() -> List[Todo]:
    return [vars(todo) for todo in todo_service.get_all_todos()]