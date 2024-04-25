while True:
    a, b = input().split()
    if a == b == '0': break
    
    a, b = list(a), list(b)
    c = 0
    qc = 0
    
    while (len(a) > 0) and (len(b) > 0):
        r = int(a.pop()) + int(b.pop()) + c
        if r >= 10:
            qc += 1
            c = 1
        else: c = 0
        
    if len(a) > 0:
        r = int(a.pop()) + c
        if r >= 10: qc+=1
    elif len(b) > 0:
        r = int(b.pop()) + c
        if r >= 10: qc+=1
        
    if qc == 0: print('No carry operation.')
    elif qc == 1: print('1 carry operation.')
    else: print(f'{qc} carry operations.')