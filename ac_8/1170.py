import math

def main():
    num = int(input())
    dias = 0
    while num > 0:
        num -=1
        comida = float(input())
        comidaInicial = comida
        while comida > 1:
            comida = comida / 2
        count = (comidaInicial / comida)
        dias = math.log(count, 2)
        print(f"{int(dias)} dias")

main()