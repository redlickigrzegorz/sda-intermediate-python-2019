from dataclasses import dataclass, field

# @dataclass(frozen=True)
from datetime import datetime, timedelta


def default_deadline() -> datetime:
    return datetime.now() + timedelta(days=2)


@dataclass
class PrioritizedTask:
    name: str
    description: str
    priority: int = field(default=0)
    deadline: datetime = field(default_factory=default_deadline)

    def __repr__(self):
        return f'{self.name}: {self.description}'

    def __lt__(self, other: 'PrioritizedTask') -> bool:
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority > other.priority


task_01 = PrioritizedTask('Sprzatanie', 'Posprzataj pokoj', 0, datetime(2019, 5, 1))
task_02 = PrioritizedTask('Spacer', 'Zabierz psa', 4, datetime(2019, 6, 1))
task_03 = PrioritizedTask('Smieci', 'wynies smieci', 4, datetime(2019, 4, 1))
task_04 = PrioritizedTask('Samochod', 'Zatankuj', 2)
task_05 = PrioritizedTask('Zakupy', 'Cos na obiad', 0)


if __name__ == '__main__':
    print(default_deadline())
