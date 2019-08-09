from dataclasses import dataclass, field
from datetime import datetime, timedelta

from src.to_do.base_list import BaseTask


def default_deadline() -> datetime:
    return datetime.now() + timedelta(days=2)


# @dataclass(frozen=True)
@dataclass
class PrioritizedTask(BaseTask):
    priority: int = field(default=0)
    deadline: datetime = field(default_factory=default_deadline)

    def __lt__(self, other: 'PrioritizedTask') -> bool:
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority > other.priority


prioritized_task_01 = PrioritizedTask('Sprzatanie', 'Posprzataj pokoj', priority=0, deadline=datetime(2019, 5, 1))
prioritized_task_02 = PrioritizedTask('Spacer', 'Zabierz psa', priority=4, deadline=datetime(2019, 6, 1))
prioritized_task_03 = PrioritizedTask('Smieci', 'wynies smieci', priority=4, deadline=datetime(2019, 4, 1))
prioritized_task_04 = PrioritizedTask('Samochod', 'Zatankuj', priority=2)
prioritized_task_05 = PrioritizedTask('Zakupy', 'Cos na obiad', priority=0)
