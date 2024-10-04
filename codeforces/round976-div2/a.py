from math import log

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = 0
    while n != 0:
        if k == 1: x = 1
        else: x = int(log(n, k))
        q = int((k**x - n) / -k**x) + 1
        
        n = n - (q * (k**x))
        s += q
        
    print(s)