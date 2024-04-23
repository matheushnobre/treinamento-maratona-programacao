i = {'W': 1, 'H': 0.5, 'Q': 0.25, 'E': 0.125, 'S': 0.0625, 'T': 0.03125, 'X': 0.015625}

while True:
    e = input().split('/')
    if e[0] == '*': break

    dc = 0
    for c in e:
        d = 0
        for n in c:
            d += i[n]   
        if d == 1:
            dc += 1
    
    print(dc)