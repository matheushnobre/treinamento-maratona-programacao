a, b = map(int, input().split())
if b <= 2:
    print('nova')
elif b <= 96 and b > a:
    print('crescente')
elif b <= 96 and b < a:
    print('minguante')
else:
    print('cheia')