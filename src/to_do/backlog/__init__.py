import typing
from dataclasses import dataclass, field

from src.to_do.backlog.task import BacklogTask
from src.to_do.base_list import BaseListTask
from src.to_do.value_objects import TaskStatus


@dataclass
class Backlog(BaseListTask):
    tasks: typing.List[BacklogTask] = field(default_factory=list)
    completed_tasks: typing.List[BacklogTask] = field(default_factory=list)

    def add_task(self, task: BacklogTask) -> None:
        task.status = TaskStatus.PENDING
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[BacklogTask]:
        if len(self.tasks) == 0:
            return None
        task = self.tasks.pop()
        task.status = TaskStatus.STARTED
        return task

    def complete_task(self, task: BacklogTask) -> None:
        task.status = TaskStatus.COMPLETED
        self.completed_tasks.append(task)
