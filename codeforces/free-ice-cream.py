n, sorv = map(int, input().split())
d = 0
for _ in range(n):
    o, q = input().split()
    if o == '+': sorv += int(q)
    else:
        if int(q) > sorv: d+=1
        else: sorv -= int(q)

print(sorv, d)