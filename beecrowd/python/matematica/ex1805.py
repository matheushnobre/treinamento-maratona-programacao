a, b = map(int, input().split())
sa = ((a-1) * (a)) // 2
sb = (b * (b+1)) // 2 - sa
print(sb)