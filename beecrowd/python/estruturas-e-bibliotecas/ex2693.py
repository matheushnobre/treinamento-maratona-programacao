while True:
    try:
        q = int(input())
        alunos = []
        
        for i in range(q):
            a, s, c = input().split()
            c = int(c)
            alunos.append((a, s, c))
        
        alunos.sort(key=lambda x:(x[2], x[1], x[0]))
        for al in alunos:
            print(al[0])
            
    except EOFError: break