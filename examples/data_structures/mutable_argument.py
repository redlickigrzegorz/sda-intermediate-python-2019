import typing
from datetime import datetime


def add_dogs(name: str, dogs: typing.List[str] = []) -> typing.List[str]:
    dogs.append(name)
    return dogs


def add_dogs_properly(name: str, dogs: typing.List[str] = None) -> typing.List[str]:
    dogs = dogs or []
    # if dogs is None:
    #     dogs = []
    dogs.append(name)
    return dogs


def print_dt(dt: datetime = datetime.now()) -> None:
    print(dt)


def print_dt_properly(dt: datetime = None) -> None:
    dt = dt or datetime.now()
    print(dt)


if __name__ == "__main__":

    print(add_dogs("Reksio"))
    print(add_dogs("Reksio", []))
    print(add_dogs("Pimpek"))
    print(add_dogs("Pimpek"))

    print("################ --> properly")
    print(add_dogs_properly("Reksio"))
    print(add_dogs_properly("Reksio", []))
    print(add_dogs_properly("Pimpek"))
    print(add_dogs_properly("Pimpek"))

    a = None
    b = 1
    print(bool(a and b))
    print(bool(a or b))
    print(a and b)
    print(b and a)
    print(a or b)
    print(b or a)

    print("################")
    print_dt()
    print_dt()
    print_dt()
    print_dt()
    print_dt()

    print("################ --> properly")
    print_dt_properly()
    print_dt_properly()
    print_dt_properly()
    print_dt_properly()
    print_dt_properly()
