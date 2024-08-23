b, r = map(int, input().split())
garantido = [0 for i in range(b+1)]
s = 0

for _ in range(r):
    a, c, p1, p2 = map(int, input().split())
    if p1 != 0 and p1 == p2:
        if garantido[a] == 0:
            garantido[a] = 1
            s += 1
        if garantido[c] == 0:
            garantido[c] = 1
            s += 1

print(s)