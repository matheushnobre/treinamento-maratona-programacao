n = int(input())
l = set([i for i in range(1, n+1)])

e = set([int(i) for i in input().split()])
print(*l.difference(e))