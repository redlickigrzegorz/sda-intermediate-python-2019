from dataclasses import dataclass, field
from datetime import datetime, timedelta

from src.to_do.base_list import BaseTask


@dataclass
class SequentialTask(BaseTask):
    status: str = field(default='just created')
    created_at: datetime = field(default_factory=datetime.now)

    def mark_task_as_completed(self):
        self.status = 'completed'


task_01 = SequentialTask('Nauka', 'Zadanie_01')
task_02 = SequentialTask('Sprzątanie', 'Posprzątaj łazienkę')
task_03 = SequentialTask('Sprzątanie', 'Posprzątaj łazienkę3')

if __name__ == '__main__':
    print(task_01.created_at)
    print(task_03.created_at)





