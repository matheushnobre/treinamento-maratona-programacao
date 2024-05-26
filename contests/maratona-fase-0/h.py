from math import sqrt

def ehPrimo(num):
    if num == 1: 
        return False
    elif num == 2: 
        return True
    else:
        for i in range(2, int(sqrt(num)+1)):
            if num % i == 0:
                return False
        return True
    
testes = int(input())
for t in range(testes):
    num = int(input())
    
    x, y = num//2, num//2+1
    
    while True:
        if x == 0:
            print(-1)
            break
        elif ehPrimo(x) or ehPrimo(y):
            x -= 1
            y += 1
        else:
            print(x, y)
            break