import typing
import collections
from dataclasses import dataclass, field
from src.to_do.sequential.task import task_01
from src.to_do.sequential.task import task_02
from src.to_do.sequential.task import task_03


from src.to_do.base_list import BaseListTask
from src.to_do.sequential.task import SequentialTask


@dataclass
class SequentialList(BaseListTask):
    tasks: typing.Deque[SequentialTask] = field(default_factory=collections.deque)

    def add_task(self, task: SequentialTask) -> None:
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[SequentialTask]:
        if len(self.tasks) == 0:
            return None
        return self.tasks.popleft()

    def remove_task(self, task: SequentialTask) -> None:
        self.tasks.remove(task)
