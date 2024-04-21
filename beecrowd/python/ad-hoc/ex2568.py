d, i, x, f = map(int, input().split())

for j in range(d+1, d+f+1):
    if j % 2 == 0:
        i += x
    else:
        i -= x
        
print(i)