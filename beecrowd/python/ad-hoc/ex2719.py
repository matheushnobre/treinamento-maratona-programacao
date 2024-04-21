t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    p = [int(i) for i in input().split()]
    k = 1
    pt = 0
    for i in p:
        pt += i
        if pt > m:
            pt=i
            k+=1
    print(k)