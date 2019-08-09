import abc
from dataclasses import dataclass, field

from src.to_do.base_list.task import BaseTask


@dataclass
class BaseListTask(abc.ABC):
    name: str = field(default='')

    @abc.abstractmethod
    def add_task(self, task: BaseTask) -> None:
        pass

    @abc.abstractmethod
    def get_task(self) -> BaseTask:
        pass

    @abc.abstractmethod
    def complete_task(self, task: BaseTask) -> None:
        pass
