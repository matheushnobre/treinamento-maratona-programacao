n = int(input())
for i in range(n):
    t = input()
    if t[0] == t[2]: s = int(t[0]) * int(t[2])
    elif t[1].islower(): s = int(t[0]) + int(t[2])
    else: s = int(t[2]) - int(t[0])
    print(s)