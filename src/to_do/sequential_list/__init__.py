import typing
from collections import deque
from dataclasses import dataclass, field

from src.to_do.base_list import BaseListTask
from src.to_do.sequential_list.task import SequentialTask


@dataclass
class SequentialList(BaseListTask):
    tasks: typing.Deque[SequentialTask] = field(default_factory=deque)

    def add_task(self, task: SequentialTask) -> None:
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[SequentialTask]:
        if len(self.tasks) == 0:
            return None
        return self.tasks.popleft()
