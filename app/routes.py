from flask import (
    Flask,
    request
)
from app.database import task
import json
import logging

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


@app.route("/tasks/<int:pk>", methods=["POST", "PUT"])
def edit_task(pk):
    # existing_task = task.select_by_id(pk)
    existing_task = get_single_task(pk)  
    print(existing_task)
    # task_data = json.dumps(request.form)
    logging.debug(existing_task)
    task.update_by_id(existing_task, pk)
    return {"message": "Task updated successfully"}, 200




@app.delete("/tasks/<int:pk>")
def delete_task(pk):
    task.delete_by_id(pk)
    return "", 204

