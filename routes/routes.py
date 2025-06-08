from fastapi import APIRouter
from fastapi import HTTPException

from schemas import Task
from utils import *
from settings import *

router = APIRouter()


@router.on_event("startup")
def launch():
    global LATEST_ID
    LATEST_ID = get_latest_id(TASKS_FILE)


@router.post("/tasks/create/", response_model=Task)
def create_task(task: Task):
    tasks = read_tasks(TASKS_FILE)

    if tasks == None:
        raise HTTPException(status_code=404, detail="JSON file not found")

    LATEST_ID += 1
    task.id = LATEST_ID
    tasks.append(task)
    save_tasks(tasks)
    return task


@router.get("/tasks/showall", response_model=list[Task])
def get_tasks():
    return read_tasks(TASKS_FILE)
