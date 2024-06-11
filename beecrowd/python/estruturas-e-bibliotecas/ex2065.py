from queue import PriorityQueue

n, m = map(int, input().split())
min = 0
func = [int(i) for i in input().split()]
clientes = [int(i) for i in input().split()]

fila = PriorityQueue()
for i in range(n):
    fila.put([0, i])
    
for i in range(m):
    c = clientes[i]
    temp, id = fila.get()
    temp = temp+c*func[id]
    min = max(temp, min)
    fila.put([temp, id])
    
print(min)