"""
Programação Estruturada
Aluno: Guilherme Resende da Rocha
AC1

Exercício 1: Equações do segundo grau

"""

# Pede os parâmetros ao usuário

a = int(input("Informe o parâmetro a da equação: "))
b = int(input("Informe o parâmetro b da equação: "))
c = int(input("Informe o parâmetro c da equação: "))

# # Calcula e apresenta as raizes da equação

print("A primeira raiz da equação é: ", (-b + ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a))
print("A segunda raiz da equação é: ", (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))



print("-" * 40)

"""

Exercício 2: Anos bissextos

"""

# Pede o ano ao usuário

ano = int(input("Informe o ano: "))

# Um ano bissexto deve ser múltiplo de 4, mas anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.

print(bool(ano % 4 == 0 and (not ano % 100 == 0 or ano % 400 == 0)))