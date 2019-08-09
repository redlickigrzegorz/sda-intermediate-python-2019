import typing
from dataclasses import dataclass, field
from heapq import heappush, heappop

from src.to_do.base_list import BaseListTask
from src.to_do.prioritized_list.task import PrioritizedTask
from src.to_do.value_objects import TaskStatus


@dataclass
class PrioritizedList(BaseListTask):
    tasks: typing.List[PrioritizedTask] = field(default_factory=list)
    completed_tasks: typing.List[PrioritizedTask] = field(default_factory=list)

    def add_task(self, task: PrioritizedTask) -> None:
        task.status = TaskStatus.PENDING
        heappush(self.tasks, task)

    def get_task(self) -> typing.Optional[PrioritizedTask]:
        if len(self.tasks) == 0:
            return None
        task = heappop(self.tasks)
        task.status = TaskStatus.STARTED
        return task

    def complete_task(self, task: PrioritizedTask) -> None:
        task.status = TaskStatus.COMPLETED
        self.completed_tasks.append(task)
