letters = 'abcdefghijklmnopqrstuvwxyz'
n, k = map(int, input().split())
used = letters[:k]
s = ''
c = 0
while len(s) != n:
    s += used[c % k]
    c += 1
print(s)