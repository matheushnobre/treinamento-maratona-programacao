n = int(input())
coord = set()
s = 0

for i in range(n):
    x, y = map(int, input().split())
    c = (x, y)
    if c not in coord:
        coord.add(c)
    else:
        s = 1

print(s)