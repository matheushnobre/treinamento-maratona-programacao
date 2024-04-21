n = int(input())
p = []
for i in range(n):
    o = input().split()
    
    if len(o) == 2:
        v = int(o[1])
    
    if o == 'PUSH':
        p.append(v)
    elif o == 'POP':
        if len(p) == 0:
            print('EMPTY')
        else:
            p.pop()
    else:
        if len(p) == 0:
            print('EMPTY')
        else:
            print(min(p))