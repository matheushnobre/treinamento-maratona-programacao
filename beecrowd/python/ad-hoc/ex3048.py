n = int(input())
l = []

s = 1
for i in range(n):
    v = int(input())
    if i != 0:
        if v != l[-1]:
            s += 1
    l.append(v)

print(s)