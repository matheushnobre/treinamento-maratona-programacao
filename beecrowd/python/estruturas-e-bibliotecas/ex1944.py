p = ['F', 'A', 'C', 'E']
b = 0
n = int(input())

for _ in range(n):
    i = input().split()
    if i[0]==p[-1] and i[1]==p[-2] and i[2]==p[-3] and i[3]==p[-4]:
        del p[-4:]
        b+=1
    else:
        p = p+i
    if len(p)==0:
        p = ['F', 'A', 'C', 'E']

print(b)