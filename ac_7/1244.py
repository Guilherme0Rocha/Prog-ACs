num = int(input())

while num > 0:
    num -= 1
    lista = input().split()
    lista.sort(key = len, reverse = True)
    for i in range(len(lista)):
        print(lista[i], end = '')
        if i != len(lista) -1:
            print(' ', end = '')
    print()