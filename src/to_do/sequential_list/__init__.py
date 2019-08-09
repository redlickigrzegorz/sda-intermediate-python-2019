import typing
from collections import deque
from dataclasses import dataclass, field

from src.to_do.base_list import BaseListTask
from src.to_do.sequential_list.task import SequentialTask
from src.to_do.value_objects import TaskStatus


@dataclass
class SequentialList(BaseListTask):
    tasks: typing.Deque[SequentialTask] = field(default_factory=deque)
    completed_tasks: typing.List[SequentialTask] = field(default_factory=list)

    def add_task(self, task: SequentialTask) -> None:
        task.status = TaskStatus.PENDING
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[SequentialTask]:
        if len(self.tasks) == 0:
            return None
        task = self.tasks.popleft()
        task.status = TaskStatus.STARTED
        return task

    def complete_task(self, task: SequentialTask) -> None:
        task.status = TaskStatus.COMPLETED
        self.completed_tasks.append(task)
