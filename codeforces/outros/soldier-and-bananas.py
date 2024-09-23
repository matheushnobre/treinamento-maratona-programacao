k, n, w = map(int, input().split())

t = 0
for i in range(1, w+1):
    t += i*k

e = t - n
if e < 0: e = 0
print(e)