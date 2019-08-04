from dataclasses import dataclass

from src.to_do.base_list import BaseTask


@dataclass
class BacklogTask(BaseTask):
    pass


task_01 = BacklogTask('Sprzatanie', 'Posprzataj pokoj')
task_02 = BacklogTask('Spacer', 'Zabierz psa')
task_03 = BacklogTask('Smieci', 'wynies smieci')
task_04 = BacklogTask('Samochod', 'Zatankuj')
task_05 = BacklogTask('Zakupy', 'Cos na obiad')


