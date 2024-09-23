n = int(input())
lista = [int(i) for i in input().split()]

s=0
for i in range(n):
    cont = 1
    j=i
    while(j>0):
        if lista[j-1] <= lista[j]:
            cont+=1
            j-=1
        else: break
    j=i
    while(j<n-1):
        if lista[j+1] <= lista[j]:
            cont+=1
            j+=1
        else: break
    if cont > s: s=cont
    
print(s)