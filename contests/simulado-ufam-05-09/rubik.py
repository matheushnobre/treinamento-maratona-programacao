MOD = 10**9 + 7
n = int(input())
e = pow(2, n) - 2
a = pow(4, e, MOD)
b = (6 * a) % MOD      
print(b)
