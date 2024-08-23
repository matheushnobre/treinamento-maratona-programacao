t = int(input())
for _ in range(t):
    n = int(input())
    seating = [int(i) for i in input().split()]
    bus = [0] * n
    
    isOk = True
    bus[seating[0]-1] = 1
    for i in range(1, n):
        sentar = seating[i]-1
        
        if sentar != 0 and sentar < n-1:
            if bus[sentar-1] == 0 and bus[sentar+1] == 0:
                isOk = False
                break
        elif sentar == 0:
            if bus[sentar+1] == 0:
                isOk = False
                break
        elif sentar == n-1:
            if bus[sentar-1] == 0:
                isOk = False
                break       
        bus[sentar] = 1
                  
    if isOk: print('YES')
    else: print('NO')