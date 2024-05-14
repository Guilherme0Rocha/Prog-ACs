import math

def main():
    while True:
        try:

            degraus = int(input())

            medidas = input().split(" ")
            h = int(medidas[0])
            c = int(medidas[1])
            l = int(medidas[2])

            hip = math.sqrt((int(c)**2)+(int(h)**2))
            hip *= (int(l)/100*int(degraus))/100
            print('%.4f'%hip)
        except EOFError:
            break

main()