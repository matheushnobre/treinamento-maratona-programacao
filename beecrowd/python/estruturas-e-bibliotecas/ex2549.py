from operator import itemgetter


while True:
    try:
        d = {}
        e = input()
        for l in e:
            try:
                d[l] += 1
            except KeyError:
                d[l] = 1
        
        d = sorted(d.items(), key=itemgetter(1, 0))
        
        for v in d:
            print(ord(v[0]), v[1], sep=' ')
        print('')       
    except EOFError: 
        break