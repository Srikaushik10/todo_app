from fastapi import FastAPI
from apps.routes.todo_route import router as todo_route

app = FastAPI(title="FastAPI-ToDo-APP")

# Register the router
app.include_router(todo_route, prefix="/todos", tags=["Todos"])

@app.get("/")
def root():
    return {"message": "Welcome to the Todo App!"}
