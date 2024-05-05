direcoes = ['N', 'L', 'S', 'O']

def localizar(arena, n, m):
    for i in range(n):
        for j in range(m):
            if arena[i][j] in direcoes:
                return i, j, arena[i][j]

while True:
    n, m, s = map(int, input().split())
    if n == m == s == 0: break
    
    arena = []
    for i in range(n):
        arena.append(list(input()))
    sent = input()
    lin, col, dir = localizar(arena, n, m)
    fig = 0
    
    for com in sent:
        if com == 'D':
            dir = direcoes[(direcoes.index(dir)+1) % 4]
        elif com == 'E':
            dir = direcoes[(direcoes.index(dir)-1) % 4]
        else:
            if dir == 'N':
                nl, nc = lin-1, col 
            elif dir == 'L':
                nl, nc = lin, col+1 
            elif dir == 'S':
                nl, nc = lin+1, col 
            elif dir == 'O':
                nl, nc = lin, col-1
            
            isPossivel = True
            try:
                if arena[nl][nc] == '#':
                    isPossivel = False
            except IndexError:
                isPossivel = False
            if nl < 0 or nc < 0:
                    isPossivel = False
        
            if isPossivel:
                if arena[nl][nc] == '*':
                    fig += 1
                arena[nl][nc] = dir
                arena[lin][col] = '.'
                lin, col = nl, nc
    
    print(fig)