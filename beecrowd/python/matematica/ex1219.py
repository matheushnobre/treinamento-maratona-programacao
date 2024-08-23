from math import sqrt

PI = 3.1415926535897
while True:
    try: 
        a, b, c = map(int, input().split())
        p = (a+b+c)/2
        a2 = sqrt(p*(p-a)*(p-b)*(p-c))
        
        r = (a * b * c) / (4 * a2)
        a1 = (PI * r**2) - a2
        
        r = a2 / ((a+b+c) / 2)
        a3 = PI * r**2
        
        a2 -= a3
        print(f'{a1:.4f} {a2:.4f} {a3:.4f}')
    except EOFError:
        break