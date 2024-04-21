n = int(input())

for i in range(n):
    m1, v1 = map(int, input().split('x'))
    v2, m2 = map(int, input().split('x'))
    
    if (m1+m2) > (v1+v2):
        print('Time 1')
    elif (m1+m2) < (v1+v2):
        print('Time 2')
    else:
        if v1 > m2:
            print('Time 2')
        elif v1 < m2:
            print('Time 1')
        else:
            print('Penaltis')