from math import gcd

def main():
    num = int(input())

    while num > 0:
        num -= 1

        cartas = input().split(" ")
        f1, f2 = int(cartas[0]), int(cartas[1])

        print(gcd(f1, f2))
main()