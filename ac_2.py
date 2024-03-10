"""
Programação Estruturada
Aluno: Guilherme Resende da Rocha
AC2

Exercício 1: Revisite a AC1

"""


# Define a formatação de separação
def traco(largura = 40):
    print("-" * largura)

def cabecalho(titulo):
    print(titulo)

# Define a formula a ser seguida ao calcular a equação
def eq_seg_grau(a, b, c):
    return (-b + ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a) , (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a)

# Define a fórmula para checar se um ano é bissexto ou não
def bissexto(ano):
    return (ano % 4 == 0 and (not ano % 100 == 0 or ano % 400 == 0))

def main1():

    # Recebe os valores para inserir na função eq_seg_grau(a, b, c) e então apresentar os resultados na tela
    traco()
    cabecalho("Equação do segundo grau:")
    a = 1
    b = -6
    c = 8
    print("As raízes da equação são:", eq_seg_grau(a, b, c))
    traco()

    traco()
    cabecalho("Ano bissexto:")

    # Recebe um ano e imprime se é bissexto o inserindo na função bissexto(ano)
    # (Exemplos:)
    ano = 2012
    print(ano, ": " , bool(bissexto(ano)) , sep = "")
    ano = 1995
    print(ano, ": " , bool(bissexto(ano)) , sep = "")
    ano = 1900
    print(ano, ": " , bool(bissexto(ano)) , sep = "")
    traco()

main1()


"""

Exercício 2: Salário

"""

# Define a fórmula para o cálculo do salário
def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    return valor_hora * num_horas - ((valor_hora * num_horas) * irpf)

def main2():

    traco()
    cabecalho("Salário:")

    # Recebe quanto é recebido por hora e a quantidade de horas para inserir na fórmula.
    valor_hora = 5.51
    num_horas = 220
    print("O salário líquido é igual a: R$" , calcula_salario(valor_hora, num_horas), sep = "")
    traco()

main2()