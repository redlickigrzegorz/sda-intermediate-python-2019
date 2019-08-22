from dataclasses import dataclass, field

from src.to_do.base_list import BaseTask



@dataclass
class DequeTask(BaseTask):
    status: str = field(default='NEW')


task_01 = DequeTask('Sprzatanie', 'Posprzataj pokoj')
task_02 = DequeTask('Spacer', 'Zabierz psa')
task_03 = DequeTask('Smieci', 'wynies smieci')
task_04 = DequeTask('Samochod', 'Zatankuj')
task_05 = DequeTask('Zakupy', 'Cos na obiad')


