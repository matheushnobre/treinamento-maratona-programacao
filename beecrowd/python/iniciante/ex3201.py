h, z, l = map(int, input().split())

if h < z < l or l < z < h:
    print('zezinho')
elif z < h < l or l < h < z:
    print('huguinho')
else:
    print('luisinho')