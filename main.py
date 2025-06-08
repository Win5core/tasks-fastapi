from fastapi import FastAPI, Request
from fastapi import FastAPI, HTTPException

# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

import json
import os

from schemas.task import Task
from utils.json_db import read_tasks, save_tasks, get_latest_id


app = FastAPI()

# Setup
TASKS_FILE = "data/tasks.json"


@app.on_event("startup")
def launch():
    global LATEST_ID
    LATEST_ID = get_latest_id(TASKS_FILE)


@app.post("/tasks/create/", response_model=Task)
def create_task(task: Task):
    tasks = read_tasks(TASKS_FILE)

    if tasks == None:
        raise HTTPException(status_code=404, detail="JSON file not found")

    LATEST_ID += 1
    task.id = LATEST_ID
    tasks.append(task)
    save_tasks(tasks)
    return task


@app.get("/tasks/showall", response_model=list[Task])
def get_tasks():
    return read_tasks(TASKS_FILE)
