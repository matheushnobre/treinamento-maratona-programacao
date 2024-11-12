t = int(input())
for _ in range(t):
    e = int(input())
    delta = (1 - 4*(-2*e)) ** (1/2)
    s = int((-1 + delta) / 2)
    print(s)