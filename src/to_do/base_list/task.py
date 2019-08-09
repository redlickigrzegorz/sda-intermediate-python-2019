from dataclasses import dataclass


@dataclass
class BaseTask:
    name: str
    description: str

    def __repr__(self):
        return f"{self.name}: {self.description}"
