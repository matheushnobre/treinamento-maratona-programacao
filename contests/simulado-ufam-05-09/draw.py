n = int(input())
emp = 0

xa, ya = 0, 0
for i in range(n):
    xi, yi = map(int, input().split())
    if xa == xi and ya == yi:
        continue
    elif xa == ya and xa != 0:
        emp += min(xi, yi) - max(xa, ya)
    elif max(xa, ya) < min(xi, yi):
        emp += min(xi, yi) - max(xa, ya) + 1
    elif max(xa, ya) == min(xi, yi):
        emp += 1 
    xa, ya = xi, yi

    
if xi == 0 and yi == 0:
    emp = 1
    
print(emp)