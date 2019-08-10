def sum_values(a, b):
    return a + b


def subtract_values(a, b):
    return a - b


s = sum_values


def make_operation(operation, a, b):
    return operation(a, b)


def make_operation2(symbol, a, b):
    def sum_values2(a, b):
        return a + b

    def subtract_values2(a, b):
        return a - b

    if symbol == '+':
        return sum_values2(a, b)
    elif symbol == '-':
        return subtract_values2(a, b)
    raise NotImplementedError()


def get_operation(symbol):
    def sum_values2(a, b):
        return a + b

    def subtract_values2(a, b):
        return a - b

    if symbol == '+':
        return sum_values2
    elif symbol == '-':
        return subtract_values2
    raise NotImplementedError()


if __name__ == '__main__':
    print(sum_values(1, 3))
    print(s(1, 3))

    print('##############################')

    print(make_operation(sum_values, 1, 3))
    print('################')

    print(make_operation2('+', 1, 3))
    print(make_operation2('-', 1, 3))
    # print(make_operation2('/', 1, 3))

    print('################')

    print(get_operation('+')(1, 3))

    sum_ints = get_operation('+')
    print(sum_ints(1, 3))
