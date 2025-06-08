# fastapi schemas

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    id: int = None  # Will be auto generated
    title: str
    done: bool = False
    kudos: Optional[int] = 0
    description: Optional[str] = ""
    created_at: Optional[int] = Field(
        default_factory=int((datetime.now().timestamp())),
        description="Only UNIX timestamp",
    )  # this will automatically make "created at". uses timestamp to reduce value size
    deleted: Optional[bool] = False
    tags: Optional[list[str]] = list(list(""))


# time = int(datetime.timestamp(datetime.now()))
# time = datetime.fromtimestamp(time)
