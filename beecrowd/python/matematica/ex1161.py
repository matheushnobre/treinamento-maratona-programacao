def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fatorial(n-1)
    
while True:
    try:
        m, n = map(int, input().split())
        print(fatorial(m) + fatorial(n))
    except EOFError:
        break