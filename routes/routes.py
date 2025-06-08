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


@router.delete("/api/tasks/delete/{id}", response_model=Task)
def delete_task(id: int):
    """Delete a task by its id"""

    TASKS[id].deleted = True
    save_tasks(TASKS, TASKS_FILE)

    return TASKS[id]


@router.put("/api/tasks/edit/{id}", response_model=list)
def edit_task(id: int, task: Task):
    """Edit a task. Delete line to not modify"""

    old_task = TASKS[id]

    TASKS[id].title = task.title
    TASKS[id].done = task.done
    TASKS[id].kudos = task.kudos
    TASKS[id].description = task.description
    TASKS[id].deleted = task.deleted
    TASKS[id].tags = task.tags

    save_tasks(TASKS, TASKS_FILE)

    return ["changed task:", old_task, "to:", TASKS[id]]
