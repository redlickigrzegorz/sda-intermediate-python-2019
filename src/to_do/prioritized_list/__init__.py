import typing
from dataclasses import dataclass, field
from heapq import heappop, heappush

from src.to_do.base_list import BaseListTask
from src.to_do.prioritized_list.task import PrioritizedTask


@dataclass
class PrioritizedList(BaseListTask):
    tasks: typing.List[PrioritizedTask] = field(default_factory=list)

    def add_task(self, task: PrioritizedTask) -> None:
        heappush(self.tasks, task)

    def get_task(self) -> typing.Optional[PrioritizedTask]:
        if len(self.tasks) == 0:
            return None
        return heappop(self.tasks)
