a = list(map(int, input().split()))
a.sort()

if a[0] == a[1] or a[1] == a[2]:
    print('S')
elif a[0] + a[1] == a[2]:
    print('S')
else:
    print('N')