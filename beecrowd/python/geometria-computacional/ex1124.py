from math import sqrt

while True:
    l, c, r1, r2 = map(int, input().split())
    if l == 0: break
    if 2*r1 > l or 2*r1 > c or 2*r2 > l or 2*r2 > c:
        print('N')
    elif sqrt((l-r2-r1)**2 + (c-r2-r1)**2) < r1+r2:
        print('N')
    else:
        print('S')