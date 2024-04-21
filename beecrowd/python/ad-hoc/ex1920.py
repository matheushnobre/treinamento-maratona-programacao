from math import sqrt

def distancia(x, y, cx, cy, r1, r2):
    d = sqrt((cx-x)**2 + (cy-y)**2)
    if d < r1: return 1
    elif d <= r2: return 2
    else: return 0

while True:
    n = int(input())
    if n == 0: break
    cd, cb, pd, pb = 0, 0, 0, 0

    cx, cy, r1, r2 = map(int, input().split())
    for i in range(2*n):
        x, y = map(int, input().split())
        r = distancia(x, y, cx, cy, r1, r2)
        
        if r == 1:
            if i % 2 == 0:
                cd += 1
            else:
                pd += 1
        elif r == 2:
            if i % 2 == 0:
                cb += 1
            else:
                pb += 1
                
    if cd > pd:
        print('C > P')
    elif cd < pd:
        print('P > C')
    elif cb > pb:
        print('C > P')
    elif cb < pb:
        print('P > C')
    else:
        print('C = P')