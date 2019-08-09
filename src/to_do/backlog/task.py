from dataclasses import dataclass

from src.to_do.base_list import BaseTask


@dataclass
class BacklogTask(BaseTask):
    pass


backlog_task_01 = BacklogTask('Sprzatanie', 'Posprzataj pokoj')
backlog_task_02 = BacklogTask('Spacer', 'Zabierz psa')
backlog_task_03 = BacklogTask('Smieci', 'wynies smieci')
backlog_task_04 = BacklogTask('Samochod', 'Zatankuj')
backlog_task_05 = BacklogTask('Zakupy', 'Cos na obiad')
