n, c, m = map(int, input().split())

car = [int(i) for i in input().split()]
com = [int(i) for i in input().split()]

s = c
for f in com:
    if f in car:
        s -= 1
        car.remove(f)

print(s)