from enum import Enum


class TaskStatus(Enum):
    NEW = "NEW"
    PENDING = "PENDING"
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
