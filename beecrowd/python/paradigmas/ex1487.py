ct = 0
while True:
    ct += 1
    n, t = map(int, input().split())
    if n == 0: break
    
    dp = [0]*(t+1)
    for i in range(n):
        d, p = map(int, input().split())
        for j in range(d, t+1):
            dp[j] = max(dp[j], p + dp[j-d])
    
    print(f'Instancia {ct}')
    print(dp[-1])
    print()