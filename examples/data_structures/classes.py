class Animal:
    pass


class Dog(Animal):
    def bark(self):
        return "how how"


class Duck(Animal):
    def quack(self):
        return "quack quack"


class Human:
    def say_something(self):
        return "Good morning!"


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

    print(hasattr(duck, "quack"))
    print(getattr(duck, "quack")())  # print(duck.quack())
    print(hasattr(duck, "say_something"))
    print(hasattr(human, "say_something"))

    print(dir(human))
