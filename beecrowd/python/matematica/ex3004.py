n = int(input())

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    if (x1 < x2 and y1 < y2) or (x1 < y2 and y1 < x2 ):
        print('S')
    else:
        print('N')