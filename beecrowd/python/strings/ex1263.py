while True:
    try:
        s=0
        aux=0
        la = None
        entrada = input().split()

        for e in entrada:
            if e[0].lower()==la:
                if aux==0:
                    s+=1
                aux+=1
            else:
                la=e[0].lower()
                aux=0
        
        print(s)
    
    except EOFError: break