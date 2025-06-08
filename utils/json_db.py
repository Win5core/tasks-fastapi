# json db config


import json
from pathlib import Path
from typing import List
from schemas.task import Task


def read_tasks(file_location) -> List[Task]:
    data_file = Path(file_location)
    if not data_file.exists():
        return None

    with open(data_file, "r") as f:
        data = json.load(f)

        tasks = []
        for item in data:
            task = Task(**item)
            tasks.append(task)

        return tasks


def save_tasks(users: List[Task], save_location):
    data_file = Path(save_location)
    with open(data_file, "w") as f:
        user_dicts = []
        for user in users:
            user_dict = user.dict()
            user_dicts.append(user_dict)

        json.dump(user_dicts, f, indent=2)  # indent=2 makes files easier to read
