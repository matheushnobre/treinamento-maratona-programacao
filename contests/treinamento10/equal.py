t = int(input())
for i in range(t):
    n = int(input())
    boxes = [int(i) for i in input().split()]
    menor = min(boxes)
    eat = 0
    for b in boxes:
        eat += b-menor
    print(eat)