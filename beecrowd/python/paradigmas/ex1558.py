from math import sqrt

numbers = {}
quadrados = []
for num in range(10001):
    if sqrt(num) % 1 == 0:
        quadrados.append(num)
        numbers[num] = True
    else:
        numbers[num] = False
        
while True:
    try:
        n = int(input())
    except EOFError:
        break
    
    ehPossivel = False
    for v in quadrados:
        if v > n:
            break
        x = n - v
        if numbers[x]:
            ehPossivel = True
            break
    
    if ehPossivel:
        print('YES')
    else:
        print('NO')