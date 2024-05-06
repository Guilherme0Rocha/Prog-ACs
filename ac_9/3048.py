def main():
    tamanho = int(input())
    sequencia = []
    while tamanho > 0:
        tamanho -= 1
        numero = input()
        if not sequencia:
            sequencia.append(numero)
        elif numero != sequencia[-1]:
            sequencia.append(numero)
    print(len(sequencia))


main()