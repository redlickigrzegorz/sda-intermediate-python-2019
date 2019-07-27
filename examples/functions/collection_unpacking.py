
if __name__ == '__main__':

    course = (2019, 'SDA', 'bootcamp')
    year, company, genre = course

    print(year)
    print(company)
    print(genre)

    year, _, _ = course

    print(year)

    nums = (1, 2, 3, 4, 5, 6)
    new = (nums[0], nums[-1])
    print(new)
    first, *rest, last = nums
    print(first)
    print(rest)
    print(last)

    first, *rest, middle, last = nums
    print(first)
    print(rest)
    print(middle)
    print(last)


    d = {
        'a': 1,
        'b': 2,
        'c': 3,

    }
    for key, value in d.items():
        print(key)
        print(value)

    t_list = [('a', 1), ('b', 2), ('c', 3)]
    di={}
    for key, value in t_list:
        di[key]=value
    print(di)

    di2={key:value for key, value in t_list}
    print(di2)

    di3=dict(t_list)
    print(di3)

    print([[key, value] for key, value in d.items()])

    items = [item for item in d.items()]
    items[0] = "zmieniłem się"
    print(items)

    tuple_list = [(1,), (2,), (3,)]
    result = []
    for item in tuple_list:
        result.append(item)
    print(result)
    result = [item for item in tuple_list]
    print(result)
