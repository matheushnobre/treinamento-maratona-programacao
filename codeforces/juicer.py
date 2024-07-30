n, b, d = map(int, input().split())
lar = [int(i) for i in input().split()]

tt=s=0
for l in lar:
    if l<=b:
        tt+=l
        if tt>d:
            s+=1
            tt=0
print(s)