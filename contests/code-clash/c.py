while True:
    try:
        lamp = input()
        n = int(input())
        p = list(map(int, input().split()))

        s = ''
        for c in p:
            s += lamp[c-1]
        print(s)
    except EOFError: break