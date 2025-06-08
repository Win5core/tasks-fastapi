from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    id: int = None  # Will be auto generated
    title: str
    done: bool = False
    kudos: Optional[int] = None
    description: Optional[str] = None
    created_at: datetime = Field(
        default_factory=lambda: int(datetime.timestamp(datetime.now()))
    )  # this will automatically make "created at" if you create a new object
    tags: Optional[list[str]] = None


# time = int(datetime.timestamp(datetime.now()))
# time = datetime.fromtimestamp(time)
