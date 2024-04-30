n = int(input())

t, me = 0, None
for i in range(n):
    m, *h = map(int, input().split())
    
    s1, s2 = 0, 0
    for index in range(m-1):
        if h[index] < h[index+1]:
            s1 += h[index+1] - h[index]
    for index in range(m-1, 0, -1):
        if h[index] < h[index-1]:
            s2 += h[index-1] - h[index]
            
    s = min(s1, s2)
    if me == None:
        me = s
        t = i+1
    elif s < me:
        me = s
        t = i+1
        
print(t)