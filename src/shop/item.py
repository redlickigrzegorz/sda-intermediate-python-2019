from collections import namedtuple

Item = namedtuple("Item", ["product", "quantity"])

if __name__ == '__main__':
    a = Item('sd', 1)
    print(a)

