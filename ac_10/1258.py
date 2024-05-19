def main():
    check = False
    while True:
        casos = int(input())

        if casos == 0:
            break

        camisas = dict()

        for i in range(casos):
            nome = input()
            camisa = input().split(" ")
            camisa.append(nome)
            camisas[i] = camisa

        camisas = dict(sorted(camisas.items(), key = lambda camisa: camisa[1][2]))
        camisas = dict(sorted(camisas.items(), key = lambda camisa: camisa[1][1], reverse = True))
        camisas = dict(sorted(camisas.items(), key = lambda camisa: camisa[1][0]))

        if check:
            print()

        for i,j in camisas.items():
            print(*j, sep = " ")
        check = True
main()