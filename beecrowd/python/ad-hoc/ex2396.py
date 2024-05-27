n, m = map(int, input().split())
comp = {int(i) : 0 for i in range(1, n+1)}

for i in range(1, n+1):
    comp[i] = sum(int(i) for i in input().split())

comp = dict(sorted(comp.items(), key = lambda x : x[1]))

for i in range(3):
    print(comp[i][0])