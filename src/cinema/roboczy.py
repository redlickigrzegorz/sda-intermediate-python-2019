from datetime import datetime
import weakref

count = 0


class Bla:
    count = []
    def __init__(self, a):
        self.__class__.count.append(weakref.proxy(self))
        self.a = a



if __name__ == '__main__':
    a = Bla(1)
    print(a.a)
    b = Bla(2)
    print(b.a)


    print(isinstance(a, Bla))
    print(Bla.count)
    print(Bla.count)

    del a
    print(Bla.count)
    print(Bla.count)

    c = Bla(3)
    print('b' in locals())






