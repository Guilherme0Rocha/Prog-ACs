def main():
    func = True
    while func:
        try:
            casos = int(input())
            print()

            while casos > 0:
                casos -= 1
                pop = []
                pop2 = []
                while True:
                    arvore = input()
                    if arvore == "":
                        break
                    else:
                        pop.append(arvore)

                for i in pop:
                    lista = []
                    lista.append(i)
                    lista.append(str('{:.4f}'.format((pop.count(i) / len(pop)) * 100, 4)))
                    pop2.append(lista)


                res = []
                [res.append(x) for x in pop2 if x not in res]
                res = sorted(res)

                for i in res:
                    nome = res[res.index(i)][0]
                    porcentagem = res[res.index(i)][1]

                    print(nome, porcentagem)
                    func = False

        except EOFError:
            break
main()