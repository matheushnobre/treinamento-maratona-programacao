t = int(input())
for i in range(t):  
    n = int(input())
    if n < 2: print(2)
    else:
        print(n * (n+1) // 2 + 1)