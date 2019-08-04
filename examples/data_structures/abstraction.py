import abc

import typing


class Animal(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def say_something(self):
        pass


class Dog(Animal):
    def say_something(self):
        print('bark, bark')

    def fetch(self):
        print(f"Run {self.name}")


class Duck(Animal):
    def say_something(self):
        print('quack, quack')


class Giraffe(Animal):
    def say_something(self):
        print('mniam, mniam')


if __name__ == '__main__':
    dog = Dog('Thor')
    dog.say_something()
    dog.fetch()

    duck = Duck('Donald')
    duck.say_something()

    giraffe = Giraffe('Frania')
    giraffe.say_something()

    animals: typing.List[Animal] = [dog, duck, giraffe]

    for animal in animals:
        animal.say_something()
        animal.fetch()
