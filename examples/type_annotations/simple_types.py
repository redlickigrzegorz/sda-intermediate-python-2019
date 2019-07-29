# Function without the type annotation
# def sum_ints(a, b):
#     return a + b
#
#
# Function with declared types but in the docstring
# def sum_ints(a, b):
#     """
#     Sum of two elements
#     :param a: integer value
#     :param b: integer value
#     :return: integer value
#     """
#     return a + b


# Properly typed function
def sum_ints(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_ints(1, 2))

    # Because of the types, PyCharm is yelling here
    print(sum_ints("Ala", "ma kota"))
    print(sum_ints([1, 2, 3], [4, 5]))
    print(sum_ints(1.1, 1.2))
