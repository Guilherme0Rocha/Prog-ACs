def main():
    
    casos = int(input())

    while casos > 0:

        casos -= 1
        itens = int(input())
        precos = {}

        while itens > 0:

            itens -= 1
            item, preco = input().strip().split(" ")

            precos[item] = float(preco)

        numCompras = int(input())

        gasto = 0.0

        while numCompras > 0:

            numCompras -= 1
            item, quantidade = input().strip().split(" ")
            gasto += int(quantidade) * precos[item]

        print(f"R$ {gasto:.2f}")

main()