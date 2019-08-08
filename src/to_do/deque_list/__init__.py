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

    def get_task(self) -> DequeTask:
        if len(self.tasks) == 0:
            return None
        return self.tasks.popleft()

    def remove_task(self, task: DequeTask) -> None:
        if len(self.tasks) == 0:
            return None
        self.tasks.remove(task)

if __name__ == '__main__':

    user_list1 = DequeList('Obowiazki')
    user_list1.add_task(task_01)
    user_list1.add_task(task_02)
    user_list1.add_task(task_03)
    #print(user_list1)
    #user_list1.get_task()
    #print(user_list1)
    #user_list1.get_task()
    print(user_list1)
    user_list1.remove_task(task_02)
    print(user_list1)




