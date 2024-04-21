for i in range(4):
    x, y = map(int, input().split())
    if i == 0:
        x1, y1 = x, y
    else:
        if x == x1:
            d = y - y1
    
print(d**2)