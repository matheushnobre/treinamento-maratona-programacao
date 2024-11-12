t = int(input())
for _ in range(t):
    comeca = set()
    s = list(input())
    for i in range(len(s)-3):
        if s[i:i+4] == ['1', '1', '0', '0']:
            comeca.add(i)  
            
    q = int(input())
    for i in range(q):
        i, v = input().split()
        i = int(i)-1
        s[int(i)] = v
        
        for index in range(i, i-4, -1):
            if s[index:index+4] == ['1', '1', '0', '0']:
                comeca.add(index)
            else:
                comeca.discard(index)

        if len(comeca) > 0:
            print('YES')
        else:
            print('NO')
        