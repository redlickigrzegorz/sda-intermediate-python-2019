def sum_args(*args):
    ret = 0
    for arg in args:
        ret += arg
    return ret


def sum_kwargs(**kwargs):
    ret = 0
    for key in kwargs:
        ret += kwargs[key]
    return ret


def sum_all(*args, **kwargs):
    ret = 0
    for arg in args:
        ret += arg
    for key in kwargs:
        ret += kwargs[key]
    return ret


if __name__ == '__main__':
    print(sum_args(5, 8, 6, 3, 5))
    print(sum_kwargs(a1=5, a2=8, a3=6, a4=3, a5=5))
    print(sum_all(5, 8, a3=6, a4=3))
