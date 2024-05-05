n = int(input())
m = []
for i in range(n):
    d, t = map(int, input().split())
    m.append((d, t))
    
m.sort()
ult = m[0][1]
s = 'S'
for mon in m:
    if mon[1] > ult:
        s = 'N'
        break
    ult = mon[1]
    
print(s)