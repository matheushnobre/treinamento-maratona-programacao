cartas = {}
for i in range(1, 14):
    cartas[i] = 4

n = int(input())    
a, b = map(int, input().split())
cartas[a] -= 1
cartas[b] -= 1
if a > 10: a = 10
if b > 10: b = 10
j = a+b

a, b = map(int, input().split())
cartas[a] -= 1
cartas[b] -= 1
if a > 10: a = 10
if b > 10: b = 10
m = a+b

for c in list(map(int, input().split())):
    cartas[c] -= 1
    if c>10: c=10
    j += c
    m += c

v = min(24-j, 23-m)
if v > 10:
    v = -1
    
elif cartas[v] == 0:
    men = v
    v = -1
    for i in range(men, 14):
        if cartas[i] > 0:
            cc = cartas[i]
            if cartas[1] > 10: cc = 10
            if m+cartas[i] > 23: break
            if j+cc != 23:
                v = i
                break
            
print(v)