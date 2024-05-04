n = int(input())
l = [int(i) for i in input().split()]
l.sort()

i = 0
ma, qtd = 0, 0
while i < len(l):
    a = l.count(l[i])
    if a > qtd:
        ma = l[i]
        qtd = a
    elif a == qtd:
        ma = l[i]
    i += a
    
print(ma)