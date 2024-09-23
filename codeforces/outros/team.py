s = 0
for i in range(int(input())):
    if input().split().count('1') >= 2:
        s += 1
print(s)