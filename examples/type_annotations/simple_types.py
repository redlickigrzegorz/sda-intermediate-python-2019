# def sum_all(a, b):
#     return a + b
#
# def sum_ints(a, b):
#     """
#     Sum of two elements
#     :param a: integer value
#     :param b: integer value
#     :return:  integer value
#     """
#     return a + b

def sum_ints(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(sum_ints(1, 2))
    print(sum_ints("Ala", "ma kota"))
    print(sum_ints([1, 2, 3], [4, 5]))
    print(sum_ints(1.1, 1.2))
