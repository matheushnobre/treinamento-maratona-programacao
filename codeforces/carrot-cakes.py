n, t, k, d = map(int, input().split())

t1, t2, b = 0, d, 0
while b<n:
    if t2<=t1:
        t2 += t
    else:
        t1 += t
    b += k

if n/k % 1 == 0: tt = t*(n/k)
else: tt = t*(int(n/k+1))
to = max(t1, t2)
print('YES') if tt>to else print('NO')