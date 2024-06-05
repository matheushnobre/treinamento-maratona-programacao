imp = False
while True:
    try:    
        d = {}
        e = input()
        if imp: print('')
        else: imp = True 
        
        for l in e:
            try:
                d[ord(l)] += 1
            except KeyError:
                d[ord(l)] = 1
        
        d = sorted(d.items(), key=lambda x:(x[1], -x[0]))
        
        for v in d:
            print(v[0], v[1], sep=' ')
        
    except EOFError: 
        break