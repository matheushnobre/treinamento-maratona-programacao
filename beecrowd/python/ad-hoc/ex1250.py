n = int(input())

for i in range(n):
    t = int(input())
    a = [int(i) for i in input().split()]
    p = input()
    
    k = 0
    for j in range(t):
        if p[j] == 'J' and a[j] > 2:
            k += 1
        elif p[j] == 'S' and a[j] <= 2:
            k += 1   
    
    print(k)