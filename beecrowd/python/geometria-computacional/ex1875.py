c = int(input())
for i in range(c):
    p = int(input())
    r, g, b = 0, 0, 0
    for j in range(p):
        m, s = input().split()
        if m == 'R' and s == 'G':
            r += 2
        elif m == 'R' and s == 'B':
            r += 1
        elif m == 'G' and s == 'R':
            g += 1
        elif m == 'G' and s == 'B':
            g += 2
        elif m == 'B' and s == 'R':
            b += 2
        else:
            b += 1
    if r == g == b:
        print('trempate')
    elif r > g and r > b:
        print('red')
    elif g > r and g > b:
        print('green')
    elif b > g and b > r:
        print('blue')
    else:
        print('empate')