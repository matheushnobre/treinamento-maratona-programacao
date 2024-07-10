n = int(input())
k = int(input())

al = []
for _ in range(n):
    al.append(int(input()))
    
c = k
al.sort(reverse=True)
for i in range(k, n):
    if al[i] == al[k-1]:
        c += 1
        
print(c)