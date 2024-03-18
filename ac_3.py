"""
Programação Estruturada
Aluno: Guilherme Resende da Rocha
AC3

"""

"""
Exercício 1: Triângulos
"""

def determina_tipo_triangulo(x, y, z):
    # Checa se os lados formam um triângulo válido
    if x + y > z and x + z > y and y + z > x:
        # Checa se todos os lados são iguais
        if x == y == z:
            return "É um Triângulo Equilátero"
        # Checa se ao menos 2 lados são iguais
        elif x == y or x == z or y == z:
            return "É um Triângulo Isósceles"
        # Checa se todos os lados são diferentes
        elif x != y or x != z or y != z:
            return "É um Triângulo Escaleno"
    else:
        return "Não é um Triângulo"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

print("-" * 30)

testa_triangulo()

print("-" * 30)
"""
Exercício 2: Dia da semana
"""

def dia_semana(dia):
    """
    Checa se o número recebido é um dia da semana válido.
    """
    if dia >= 1 and dia <= 7:
        """
        Retorna o dia correspondente, dependendo do número recebido.
        """
        if dia == 1:
            return "O dia é Domingo."
        elif dia == 2:
            return "O dia é Segunda-Feira."
        elif dia == 3:
            return "O dia é Terça-Feira"
        elif dia == 4:
            return "O dia é Quarta-Feira"
        elif dia == 5:
            return "O dia é Quinta-Feira"
        elif dia == 6:
            return "O dia é Sexta-Feira"
        elif dia == 7:
            return "O dia é Sábado"
    else:
        return ""

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

print("-" * 30)

testa_dia_semana()

print("-" * 30)

"""
Exercício 3: Calculadora Simples
"""

def soma(num1, num2):
    """
    Define a fórmula da soma e arredonda o resultado para ter no máximo
    2 casas decimais.
    """
    return round(num1 + num2, 2)

def subtracao(num1, num2):
    """
    Define a fórmula da subtração e arredonda o resultado para ter no máximo
    2 casas decimais.
    """
    return round(num1 - num2, 2)

def multiplicacao(num1, num2):
    """
    Define a fórmula da multiplicação e arredonda o resultado para ter no
    máximo 2 casas decimais.
    """
    return round(num1 * num2, 2)

def divisao(num1, num2):
    """
    Define a fórmula da divisão e arredonda o resultado para ter no máximo
    2 casas decimais.
    """
    return round(num1 / num2, 2)

def calculadora():
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe outro número: "))
    oper = input("Informe a operação: ")

    """
    Checa qual operação deve ser executada, dependendo da string entregue
    pelo usuário, e se é uma operação válida.
    """
    if oper == "soma":
        print("Resultado:", soma(num1, num2))
    elif oper == "subtração":
        print("Resultado:", subtracao(num1, num2))
    elif oper == "multiplicação":
        print("Resultado:", multiplicacao(num1, num2))
    elif oper == "divisão":
        print("Resultado:", divisao(num1, num2))
    else:
        print("Operação inválida.")

print("-" * 30)

calculadora()

print("-" * 30)