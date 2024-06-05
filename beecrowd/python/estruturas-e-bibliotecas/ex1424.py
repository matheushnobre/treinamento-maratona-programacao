while True:
    try:
        n, m = map(int, input().split())
        dic = {}
        vet = [int(i) for i in input().split()]
        for i, v in enumerate(vet):
            try:
                dic[v].append(i+1)
            except KeyError:
                dic[v] = [i+1]
                
        for i in range(m):
            k, v = map(int, input().split())
            try:
                p = dic[v][k-1]
            except IndexError:
                p = 0
            except KeyError:
                p = 0
            print(p)
    except EOFError: break