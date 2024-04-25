def isPrime(n):
    if n == 1: return False
    
    i=2
    while i*i <= n:
        if n % i == 0: 
            return False
        i += 1
        
    return True

n = int(input())

for i in range(n):
    x = int(input())
    print('Prime') if isPrime(x) else print('Not Prime')