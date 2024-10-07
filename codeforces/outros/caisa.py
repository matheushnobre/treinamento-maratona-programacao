n = int(input())
pylons = list(map(int, input().split()))
e = 0
ans = pylons[0]

for i in range(1, n):
    e += pylons[i-1] - pylons[i]
    if e < 0:
        ans += abs(e)
        e = 0
        
print(ans)