n = int(input())
for i in range(n):
    t = input()
    s1, s2 = 0, 0
    for j in range(3):
        s1 += int(t[j])
    for j in range(3, 6):
        s2 += int(t[j])
    if s1 == s2:
        print('YES')
    else:
        print('NO')