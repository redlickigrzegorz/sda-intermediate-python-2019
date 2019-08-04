from dataclasses import dataclass, field
import abc


@dataclass
class BaseListTask(abc.ABC):
    name: str = field(default='')

    @abc.abstractmethod
    def add_task(self, task):
        pass

    @abc.abstractmethod
    def get_task(self):
        pass
