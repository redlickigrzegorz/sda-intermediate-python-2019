if __name__ == "__main__":
    a = 1
    b = 2
    print(f"a = {a}")
    print(f"b = {b}")
    temp = b
    print(f"temp = {temp}")
    b = a
    a = temp
    print(f"a = {a}")
    print(f"b = {b}")

    print("#############")
    c = 4
    d = 6
    print(f"c = {c}")
    print(f"d = {d}")
    temp = (c, d)
    print(f"temp = {temp}")
    d, c = temp
    print(f"c = {c}")
    print(f"d = {d}")

    print("#############")
    e = 8
    f = 10
    print(f"e = {e}")
    print(f"f = {f}")
    # temp = (e, f)
    f, e = e, f
    print(f"e = {e}")
    print(f"f = {f}")
