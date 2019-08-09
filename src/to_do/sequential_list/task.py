from dataclasses import dataclass, field
from datetime import datetime

from src.to_do.base_list import BaseTask


@dataclass
class SequentialTask(BaseTask):
    created_at: datetime = field(default_factory=datetime.now)


sequential_task_01 = SequentialTask('Sprzatanie', 'Posprzataj pokoj')
sequential_task_02 = SequentialTask('Spacer', 'Zabierz psa')
sequential_task_03 = SequentialTask('Smieci', 'wynies smieci')
sequential_task_04 = SequentialTask('Samochod', 'Zatankuj')
sequential_task_05 = SequentialTask('Zakupy', 'Cos na obiad')
