if __name__ == "__main__":
    a = 1
    b = 2
    temp = b
    b = a
    a = temp
    print(f"a= {a}")
    print(f"b= {b}")

    c = 4
    d = 6
    temp = (c, d)
    print(temp)
    d, c = temp
    print(f"c= {c}")
    print(f"d= {d}")

    e = 8
    f = 10
    # temp2 = (e, f)
    print(temp)
    f, e = e, f
    print(f"e= {e}")
    print(f"f= {f}")
