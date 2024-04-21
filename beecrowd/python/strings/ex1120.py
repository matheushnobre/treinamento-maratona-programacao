while True:
    d, n = input().split()
    if d == '0' and n == '0': break
    
    v = '' # saída
    for caractere in n:
        if caractere != d:
            v += caractere
            
    if len(v) == 0 or v.count('0') == len(v): v = '0'
    else:
        for index, caractere in enumerate(v):
            if caractere != '0':
                v = v[index:len(v)]
                break
            
    print(v)