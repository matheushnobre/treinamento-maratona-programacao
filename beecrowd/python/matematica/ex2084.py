n = int(input())
v = [int(i) for i in input().split()]

v.sort(reverse=True)
t, m = sum(v), v[0]
p = (m*100)/t

if p >= 45:
    print(1)
elif p >= 40:
    d = v[0] - v[1]
    pd = (d*100)/t
    if pd >= 10:
        print(1)
    else:
        print(2)
else:
    print(2)