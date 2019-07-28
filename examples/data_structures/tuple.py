import typing


def sum_dif(a: int, b: int)-> typing.Tuple[int, int]:
    c = a + b
    d = a - b
    return c, d


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(id(list1))
    list1.append(8)
    print(id(list1))
    tup1 = (11, 12, 14, 15)
    print(tup1.index(14))
    print(id(tup1))
    print("#######")
    list_str = ['ala ', 'ma', ' kota']
    result = ''
    for word in list_str:
        result += word
        print(id(result))
    print(result)
    # print(result[2])
    # result[2] = 'd'
    print(sum_dif(10, 2))
    s, k = sum_dif(12, 4)
    print(s)
    print(k)

    zmienna:typing.Tuple[int, str] = (1, 'pies')

    a_int = 1
    l_int = [1, 2, 3, 4]
    l_int2: typing.List[int] = []
    l_int2.append(1)
    l_int2.append("asda")
