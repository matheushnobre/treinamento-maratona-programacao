t = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
t2 = []
i = 0
for j in range(15):
    m, n = map(int, input().split())
    if j in [8, 12, 14]:
        t, t2 = t2, []
        i = 0
        
    if m > n:
        t2.append(t[i])
    else:
        t2.append(t[i+1])
    i += 2
print(t2[0])