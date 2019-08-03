import typing
from dataclasses import dataclass, field
from heapq import heappush, heappop

from src.to_do.prioritized_list.task import PrioritizedTask


@dataclass
class PrioritizedList:
    name: str = field(default='')
    tasks: typing.List[PrioritizedTask] = field(default_factory=list)

    def add_task(self, task: PrioritizedTask) -> None:
        heappush(self.tasks, task)

    def get_task(self) -> typing.Optional[PrioritizedTask]:
        if len(self.tasks) == 0:
            return None
        return heappop(self.tasks)

if __name__ == '__main__':
    new_list = []
    # heappush(new_list, (2, 3))
    # heappush(new_list, (0, 6))
    # heappush(new_list, (5, 5))
    # heappush(new_list, (0, 5))
    # heappush(new_list, task_01) # 0
    # heappush(new_list, task_02) # 4
    # heappush(new_list, task_03) # 3
    # print(heappop(new_list))
