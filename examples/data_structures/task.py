from collections import namedtuple
from dataclasses import dataclass

task_01 = {
    'name': 'Sprzatanie',
    'description': 'Posprzątaj pokój'
}


Task = namedtuple('Task', ('name', 'description'))
task_02 = Task('Sprzatanie', 'Posprzataj pokoj')


@dataclass
class TaskClass:
    name: str
    description: str

    def representation(self):
        print(f'{self.name}: {self.description}')

    def __repr__(self):
        return f'{self.name}: {self.description}'


task_03 = TaskClass('Sprzatanie', 'Posprzataj pokoj')


if __name__ == '__main__':
    print(f'{task_01["name"]}: {task_01["description"]}')
    print(f'{task_02.name}: {task_02.description}')
    task_03.representation()
    print(task_03)
