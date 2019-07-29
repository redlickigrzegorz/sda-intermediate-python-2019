if __name__ == "__main__":

    course = (2019, "SDA", "bootcamp")
    year, company, genre = course
    print(year)
    print(company)
    print(genre)

    print('#############')
    year, _, _ = course
    print(year)

    print('#############')
    nums = (1, 2, 3, 4, 5, 6)
    new = (nums[0], nums[-1])
    print(new)

    print('#############')
    first, *rest, last = nums
    print(first)
    print(rest)
    print(last)

    print('#############')
    first, *rest, middle, last = nums
    print(first)
    print(rest)
    print(middle)
    print(last)

    print('#############')
    sample_dict = {"a": 1, "b": 2, "c": 3}
    for item in sample_dict.items():
        print(f"{item[0]}: {item[1]}")

    for key, value in sample_dict.items():
        print(f"{key}: {value}")

    print('#############')
    print([[key, value] for key, value in sample_dict.items()])

    items = [item for item in sample_dict.items()]
    items[0] = "I am changed now!"
    print(items)

    print('#############')
    tuple_list = [(1,), (2,), (3,)]
    result = []
    for item in tuple_list:
        result.append(item)
    print(result)
    result = [item for item in tuple_list]
    print(result)

    print('#############')
    dict_items = [("a", 1), ("b", 2), ("c", 3)]
    dict_1 = {}
    for key, value in dict_items:
        dict_1[key] = value
    print(dict_1)

    dict_2 = {key: value for key, value in dict_items}
    print(dict_2)

    dict_3 = dict(dict_items)
    print(dict_3)
