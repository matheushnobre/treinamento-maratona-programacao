n = int(input())
fios = [int(i) for i in input().split()]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    if a-1>=0: fios[a-1] += (b-1)
    if a+1<n: fios[a+1] += (fios[a]-b)
    fios[a] = 0
    
for fio in fios:
    print(fio)