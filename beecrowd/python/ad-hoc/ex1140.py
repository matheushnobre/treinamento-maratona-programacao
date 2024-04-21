while True:
    palavras = input().split()
    if palavras[0] == '*': break
    l = palavras[0][0].lower()
    is_tautograma = True
    for palavra in palavras:
        if palavra[0].lower() != l:
            is_tautograma = False
            break
    print('Y') if is_tautograma else print('N')