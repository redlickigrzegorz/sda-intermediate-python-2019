import typing
from dataclasses import dataclass, field

from src.to_do.base_list import BaseListTask
from collections import deque
from src.to_do.deque_list.task import DequeTask, task_01, task_02, task_03


@dataclass
class DequeList(BaseListTask):
    tasks: typing.Deque[DequeTask] = field(default_factory=deque)

    def add_task(self, task: DequeTask) -> None:
        self.tasks.append(task)
        task.status = 'PENDING'

    def get_task(self) -> DequeTask:
        if len(self.tasks) == 0:
            return None
        self.tasks[0].status = 'TAKEN'
        return self.tasks.popleft()

    def remove_task(self, task: DequeTask) -> None:
        if len(self.tasks) == 0:
            return None
        self.tasks.remove(task)

    def mark_task_as_completed(self, task: DequeTask) -> typing.List[DequeTask]:
        if len(self.tasks) == 0:
            return None
        done_list = []
        if task in self.tasks:
            done_list.append(task)
            task.status = 'DONE'
        return done_list


if __name__ == '__main__':
    user_list1 = DequeList('Obowiazki')
    user_list1.add_task(task_01)
    user_list1.add_task(task_02)
    user_list1.add_task(task_03)
    # print(user_list1)
    # user_list1.get_task()
    print(user_list1)
    user_list1.get_task()
    print(user_list1)
    # user_list1.remove_task(task_02)
    # print(user_list1)
    print(task_01.status)
    print(task_02.status)
    print(task_03.status)
    print(user_list1.mark_task_as_completed(task_02))
    print(task_02.status)



