import typing

from src.to_do.backlog.task import BacklogTask


class Backlog:

    def __init__(self) -> None:
        self.tasks: typing.List[BacklogTask] = []

    def add_task(self, task: BacklogTask) -> None:
        self.tasks.append(task)

    def get_task(self) -> typing.Optional[BacklogTask]:
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop()
