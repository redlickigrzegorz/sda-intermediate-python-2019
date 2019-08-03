from dataclasses import dataclass


# @dataclass(frozen=True)
@dataclass
class BacklogTask:
    name: str
    description: str

    def __repr__(self):
        return f'{self.name}: {self.description}'


task_01 = BacklogTask('Sprzatanie', 'Posprzataj pokoj')
task_02 = BacklogTask('Spacer', 'Zabierz psa')
task_03 = BacklogTask('Smieci', 'wynies smieci')
task_04 = BacklogTask('Samochod', 'Zatankuj')
task_05 = BacklogTask('Zakupy', 'Cos na obiad')


