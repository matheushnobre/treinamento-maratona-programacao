l = [int(i) for i in input().split()]
l.sort()

a = l[0]
b = l[1]

if a + b == l[2]:
    c = l[3]
else:
    c = l[2]
    
print(a, b, c)