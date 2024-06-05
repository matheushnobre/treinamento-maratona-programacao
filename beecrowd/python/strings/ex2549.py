while True:
    try:
        n, a = input().split()
        n = int(n)
        alunos = []
        for i in range(n):
            al = ''.join([n[0] for n in input().split()])+a
            alunos.append(al)
        sd = set(alunos)
        print(len(alunos) - len(sd))        
    except EOFError: break