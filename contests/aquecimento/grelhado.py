t, a, b = map(int, input().split())
v = [a, b]
aux = 0

while(v[0] != t and v[1] != t):
    if v[0] < v[1]:
        aux += v[0]
        v = [a, b-v[0]]
    else:
        aux += v[1]
        v = [a-v[1], b]
    
print(t+aux, end='')