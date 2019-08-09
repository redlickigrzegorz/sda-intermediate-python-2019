from dataclasses import dataclass, field

from src.to_do.value_objects import TaskStatus


@dataclass
class BaseTask:
    name: str
    description: str
    status: TaskStatus = field(default=TaskStatus.NEW)

    def __repr__(self):
        return f'{self.name}: {self.description}'
