n = int(input())
for i in range(n):
    a = int(input())
    b = [int(i) for i in input().split()]
    c = int(input())
    
    d = [a, c]
    d.extend(b)
    d.sort()
    if d == [1, 2, 3, 4, 5, 6]:
        if (a+c==7) and (b[0]+b[2]==7) and (b[1]+b[3]==7):
            print('SIM')
        else:
            print('NAO')
    else:
        print('NAO')