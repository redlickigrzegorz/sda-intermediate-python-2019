import typing
from dataclasses import dataclass, field

from src.to_do.backlog.task import BacklogTask


@dataclass
class Backlog:
    name: str = field(default='')
    tasks: typing.List[BacklogTask] = field(default_factory=list)

    def add_task(self, task: BacklogTask) -> None:
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[BacklogTask]:
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop()
