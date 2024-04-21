while True:
    try:
        a, b = map(int, input().split())
        print(abs(b-a))
    except EOFError:
        break