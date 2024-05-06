def main():
    cha = int(input())
    A,B,C,D,E = input().split(' ')
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    E = int(E)
    respostas = [A,B,C,D,E]
    print(respostas.count(cha))

main()