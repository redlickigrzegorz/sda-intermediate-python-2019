class Animal:
    pass


class Dog(Animal):
    def bark(self):
        return "how how"


class Duck(Animal):
    def qua(self):
        return "qua qua"


class Human:
    def good_morning(self):
        return "good morning"


if __name__ == '__main__':
    dog = Dog()
    duck = Duck()
    human = Human()
    animal = Animal()

    print(isinstance(dog, Dog))
    print(isinstance(duck, Animal))
    print(isinstance(duck, Dog))
    print(isinstance(animal, Animal))
    print(isinstance(animal, Dog))
    print(isinstance(animal, Duck))
    print(isinstance(human, Animal))

    print(issubclass(Dog, Animal))
    print(issubclass(Animal, Dog))

    print(hasattr(duck, "qua"))
    print(getattr(duck, "qua")())  # print(duck.qua())
    print(hasattr(duck, "good_morning"))
    print(hasattr(human, "good_morning"))
    print(dir(human))
