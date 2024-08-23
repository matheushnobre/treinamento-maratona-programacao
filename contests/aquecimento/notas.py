n = int(input())
notas = [float(i) for i in input().split()]
alunos = [float(i) for i in input().split()]

c=0
for i in range(n):
    if notas[i] == alunos[i]: c+=1
print(c)