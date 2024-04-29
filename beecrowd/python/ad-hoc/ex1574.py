t = int(input())

for i in range(t):
    n = int(input())
    p, a = 0, []
    
    for i in range(n):
        c = input()
        if c == 'LEFT':
            p -= 1
            a.append(c)
        elif c == 'RIGHT':
            p += 1
            a.append(c)
        else:
            c = a[int(c.split()[2])-1]
            if c == 'LEFT':
                p -= 1
                a.append(c)
            elif c == 'RIGHT':
                p += 1
                a.append(c)
    print(p)