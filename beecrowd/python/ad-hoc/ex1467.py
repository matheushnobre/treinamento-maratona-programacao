while True:
    try:
        e = [int(i) for i in input().split()]
        if e[0] == e[1] == e[2]:
            print('*')
        else:
            m = 0 if e.count(0) == 1 else 1
            if e.index(m) == 0: print('A')
            elif e.index(m) == 1: print('B')
            else: print('C')
    except EOFError:
        break