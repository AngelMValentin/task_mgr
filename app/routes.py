from flask import (
    Flask,
    request
)
from app.database import task

app = Flask(__name__)

# ReST - Representation State Transfer
# ReST is an architectural design pattern that helps design our APIs services

@app.get("/")
@app.get("/tasks")
def get_all_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
        "ok": True
    }
    return out

@app.post("/tasks")
def create_task():
    task_data = request.json 
    task.create_task(task_data)
    return "", 204


@app.put("/tasks/<int:pk>")
def update_task(pk):
    existing_task = task.select_by_id(pk)
    if not existing_task:
        return {"error": "Task not found"}, 404  
    
    task_data = request.json  
    task.update_by_id(task_data, pk)  
    return "", 204  



@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

