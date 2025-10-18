from fastapi import FastAPI #Importing FastAPI into my Project
from app.routes.todo_route import router as todo_route
'''
creating an instance of the FastAPI application
object — app — is what your server (Uvicorn) runs to handle all HTTP requests
'''
app = FastAPI(title="FastAPI-ToDo-APP")

app.include_router(todo_route,prefix="/todos",tags=["Todos"])

@app.get("/")
def root():
    return {"message": "Welcome to the Todo App!"}

