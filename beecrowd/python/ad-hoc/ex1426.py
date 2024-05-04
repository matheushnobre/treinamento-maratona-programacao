n = int(input())

for t in range(n):
    mat = []
    for i in range(1, 6):
        e = [int(i) for i in input().split()]
        l = []
        for j in range(len(e)):
            l.append(e[j])
            if j != len(e)-1: l.append(None)
        mat.append(l)
        if i != 5: mat.append([None] * (i*2))

    for i in range(1, 9, 2):
        for j in range(0, len(mat[i]), 2):
            m1 = mat[i-1][j]
            m2 = mat[i+1][j]
            m3 = mat[i+1][j+2]
            a = (m1+m2-m3) // 2
            mat[i][j] = a
            mat[i][j+1] = m1-a
            mat[i+1][j+1] = a-m2 
            
    for linha in mat:
        print(*linha)