while True:
    try:
        n = int(input())
        m, c = 1, 1
        while m != 0:
            m = (m * 10 + 1) % n
            c += 1
        print(c)
    except EOFError:
        break
    