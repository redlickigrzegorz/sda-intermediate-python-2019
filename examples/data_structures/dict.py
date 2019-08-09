import copy

if __name__ == "__main__":
    user1 = {"name": "Marian", "age": 25}
    print(user1["name"])
    # print(user1['children'])
    print(user1.get("name"))
    print(user1.get("children", []))

    print("#############")
    user2 = {"name": "Jan", 2: "dwa", 3.23: [1, [2, [3]]]}
    print((((user2.get(3.23))[1])[1])[0])

    print("#############")
    user3 = {"name": "Mietek", 3.23: [1, [2, [3]]]}
    l = user3.get(3.23)
    print(l)
    l_deep = l[1]
    print(l_deep)
    l_deeper = l_deep[1]
    print(l_deeper)
    print(l_deeper[0])

    print("################")
    print(hash(2))
    print(hash("abc"))
    print(hash("abc"))
    # print(hash([1, 2, 3]))
    print(hash((1, 2, 3)))
    print(hash((1, 2, 3)))

    print("################")
    board = {
        (0, 0): True,
        (0, 1): False,
        (0, 2): True,
        (1, 0): False,
        (1, 1): True,
        (1, 2): False,
        (2, 0): True,
        (2, 1): False,
        (2, 2): True,
    }
    print(board)
    print(board.get((0, 2)))

    print("################")
    a = 1
    b = a
    b = 2
    print(a)
    print(b)

    print("################")
    x = [1, 2, 3]
    y = x
    print(f"x: {x}")
    print(f"y: {y}")
    y.append(4)
    print(f"x: {x}")
    print(f"y: {y}")

    print("################")
    user4 = {"name": "Ewa", "children": ["Monika", "Ewelina"]}
    user5 = user4

    print(f"user4: {user4}")
    print(f"user5: {user5}")

    user5["dogs"] = ["Pimpek", "Ciapek"]
    print(f"user4: {user4}")
    print(f"user5: {user5}")

    print("#############")
    user4 = {"name": "Ewa", "children": ["Monika", "Ewelina"]}
    user5 = user4.copy()

    print(f"user4: {user4}")
    print(f"user5: {user5}")

    user5["dogs"] = ["Pimpek", "Ciapek"]
    print(f"user4: {user4}")
    print(f"user5: {user5}")

    user6 = dict(user4)
    user6["cars"] = ["opel"]
    print(f"user4: {user4}")
    print(f"user6: {user6}")

    print("#############")
    user7 = {"name": "Ewa", "children": ["Monika", "Ewelina"]}
    user8 = user7.copy()

    print(f"user7: {user7}")
    print(f"user8: {user8}")

    user8["children"].append("Michal")

    print(f"user7: {user7}")
    print(f"user8: {user8}")

    print("#############")
    user7 = {"name": "Ewa", "children": ["Monika", "Ewelina"]}
    user8 = copy.deepcopy(user7)

    print(f"user7: {user7}")
    print(f"user8: {user8}")

    user8["children"].append("Michal")

    print(f"user7: {user7}")
    print(f"user8: {user8}")
