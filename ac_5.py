"""
Programação Estruturada
2024.01
18/03/2024

Estruturas de Repetição
AC5
"""

import random

def main():
    vida_av = 100
    vida_monstro = random.randint(60, 80)

    atq_av = random.randint(10, 20)
    atq_monstro = random.randint(20, 30)

    def_av = random.randint(1, 5)

    rodada = 1

    print("\nAtributos:")
    print("Aventureiro:", "vida", vida_av, "- atq", atq_av, "- def", def_av)
    print("Monstro:", "vida", vida_monstro, "- atq", atq_monstro)

    while vida_av > 0 and vida_monstro > 0:
        print("\nRodada", rodada)
        rodada += 1

        print("Aventureiro:", "vida", vida_av, "- atq", atq_av, "- def", def_av)
        print("Monstro:", "vida", vida_monstro, "- atq", atq_monstro)

        dano_av = random.randint(1, atq_av)
        if dano_av <= 0:
            dano_av = 0
        vida_monstro = vida_monstro - dano_av
        if vida_monstro <= 0:
            print("Monstro morreu!\n")
            break

        dano_monstro = random.randint(1, atq_monstro) - def_av
        if dano_monstro <= 0:
            dano_monstro = 0
        vida_av = vida_av - dano_monstro
        if vida_av <= 0:
            print("Aventureiro morreu!\n")
            break

main()