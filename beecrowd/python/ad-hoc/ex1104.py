while True:
    a, b = map(int, input().split())
    if a == b == 0: break

    alice = set([int(i) for i in input().split()])
    beatriz = set([int(i) for i in input().split()])

    da = len(alice.difference(beatriz))
    db = len(beatriz.difference(alice))

    print(min(da, db))