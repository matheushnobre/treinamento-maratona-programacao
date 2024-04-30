while True:
    try:
        n, m = map(int, input().split())
        l = [int(i) for i in input().split()]
        l.sort(reverse=True)
        p = sum(l[:m])
        print(p)
    except EOFError: break