n = int(input())
for a in range(n):
    l = input().split()
    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if len(l[j]) < len(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    print(" ".join(l))