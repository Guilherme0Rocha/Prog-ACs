import math

def ePrimo(n):
    if n%2 == 0 and n>2:
        return False
    return all(n%i for i in range(3,int(math.sqrt(n))+1, 2))

def main():
    casos = int(input())
    for _ in range(casos):
        num = int(input())
        if (ePrimo(num)):
            print('Prime')
        else:
            print('Not Prime')

main()