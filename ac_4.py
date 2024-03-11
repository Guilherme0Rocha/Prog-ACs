"""
Programação Estruturada
2024.1
11/03/2024

Estruturas de Decisão
AC4
"""

def ler_nome():
    """Retorna o nome do aluno."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as quatro notas das avaliações e retorna os valores."""
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    asub = float(input("Informe a nota da AS: "))
    ac = float(input("Informe a nota da AC: "))
    return ap1, ap2, asub, ac

def notas_sao_validas(ap1, ap2, asub, ac):
    """
    Retorna True se as quatro notas estão entre 0 e 10, inclusive.
    Retorna False caso contrário.
    """
    ap1_v = ap1 >= 0 and ap1 <= 10
    ap2_v = ap2 >= 0 and ap2 <= 10
    asub_v = asub >= 0 and asub <= 10
    ac_v = ac >= 0 and ac <= 10
    if ap1_v and ap2_v and asub_v and ac_v:
        return True
    else:
        return False

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as avaliações apresentadas.
    Substitui a AP1 pela AS caso AS > AP1.
    Substitui a AP2 pela AS caso AS > AP2.
    A AS só substitui uma das duas provas (a menor delas).
    Caso a AS seja menor que a AP1 e a AP2, retorna AP1 e AP2.
    """
    if asub > ap1:
        prova1 = asub
        prova2 = ap2
        return prova1 , prova2
    elif asub > ap2:
        prova1 = ap1
        prova2 = asub
        return prova1 , prova2
    else:
        prova1 = ap1
        prova2 = ap2
        return prova1 , prova2



def calcular_media(prova1, prova2, ac):
    """
    Retorna a média das avaliações, arredondando para duas casas decimais.
    M = (NOTA1 + NOTA2) * 0.4 + AC * 0.2
    """
    return round((prova1 + prova2) * 0.4 + ac * 0.2, ndigits=2)

def aluno_foi_aprovado(media):
    """
    Retorna True se o aluno tiver média superior ou igual à nota mínima de
    aprovação, e False caso contrário.
    """
    return media >= 7

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            prova1, prova2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(prova1, prova2, ac)
            if aluno_foi_aprovado(media):
                print(nome, "foi aprovado! Sua média foi: ", media)
            else:
                print(nome, "foi reprovado! Sua média foi: ", media)

main()