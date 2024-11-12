n = int(input())
p = [input() for _ in range(n)]

e = []
c = p[0]
for i in range(n):
    w = p[i]
    s = ''
    for j in range(5):
        if w[j] == c[j]:
            s += '*'
        elif w[j] in c:
            s += '!'
        else:
            s += 'X'
    e.append(s)
    
g = int(input())
for _ in range(g):
    print(e.count((input())))