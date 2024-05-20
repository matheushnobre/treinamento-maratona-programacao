def main():

    n = int(input())
    carneiros = [int(i) for i in input().split()]

    i = maxi = 0
    while 0 <= i < n:
        atual = carneiros[i]
        if i > maxi:
            maxi = i
            
        if atual != 0:
            carneiros[i] = atual - 1
        if atual % 2 == 0:
            i -= 1
        else:
            i += 1
        
    print(maxi+1, sum(carneiros))

main()