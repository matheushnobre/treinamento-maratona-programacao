n = int(input())
a, l, p = map(int, input().split())

if n <= a and n <= l and n <= p:
    print('S')
else:
    print('N')