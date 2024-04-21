ins = 1
while True:
    try:
        n = int(input())
        alunos = dict()
        for i in range(n):
            a, p = input().split()
            alunos[a] = int(p)
            
        pr = min(alunos.values())
        reprovados = [aluno for aluno in alunos.keys() if alunos[aluno] == pr]
        reprovados.sort()
        
        print(f'Instancia {ins}')
        print(reprovados[-1])
        print('')
        
        ins += 1
    except EOFError:
        break
