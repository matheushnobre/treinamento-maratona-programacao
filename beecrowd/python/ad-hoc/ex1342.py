while True:
    p, s = map(int, input().split())
    if p == s == 0: break
    
    t1, t2, t3 = map(int, input().split())
    jog = [[i+1, True, 0] for i in range(p)]
    
    n = int(input())
    vez, venc = 0, None
    for i in range(n):
        d1, d2 = map(int, input().split())
        d = d1 + d2
        
        jog[vez][2] += d
        if jog[vez][2] in [t1, t2, t3]:
            jog[vez][1] = False
        elif jog[vez][2] > s and venc == None:
            venc = vez + 1
        vez = (vez+1)%p
        
        if jog[vez][1] == False:
            while jog[vez][1] == False:
                jog[vez][1] = True
                vez = (vez+1)%p
            
    print(venc)