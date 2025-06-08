# fastapi routes


from fastapi import APIRouter
from fastapi import HTTPException

from schemas import Task
from utils import *
from settings import *

router = APIRouter()


@router.on_event("startup")
def launch():
    global TASKS

    TASKS = read_tasks(TASKS_FILE)


@router.post("/api/tasks/create/", response_model=Task)
def create_task(task: Task):
    """Create a new task"""
    TASKS = read_tasks(TASKS_FILE)

    if TASKS == None:
        raise HTTPException(status_code=404, detail="JSON file not found")

    task.id = TASKS[-1].id + 1

    TASKS.append(task)
    save_tasks(TASKS, TASKS_FILE)

    return task


@router.get("/api/tasks/showall", response_model=list[Task])
def get_all_tasks():
    """Get all tasks"""

    return TASKS


@router.get("/api/tasks/show/{id}", response_model=Task)
def get_task(id: int):
    """Get a task by its id"""

    return TASKS[id]
