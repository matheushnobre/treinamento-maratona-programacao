n = int(input())
sin = []
sin.append([int(i) for i in input().split()])

for i in range(n-1):
    l = []
    for j in range(len(sin[-1])-1):
        if sin[-1][j] == sin[-1][j+1]:
            l.append(1)
        else:
            l.append(-1)
    sin.append(l)

if sin[-1][-1] == -1:
    print('branca')
else:
    print('preta')