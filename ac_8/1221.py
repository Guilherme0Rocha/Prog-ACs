def check():
        num = int(input())
        lista =[2, 3, 4, 5, 6, 7, 8, 9, 10]
        if num in lista:
            lista.remove(num)
        for i in lista:
            if num % i == 0:
                return False

def main():
    casos = int(input())
    while casos > 0:
        try:
            if check() == False:
                print("Not Prime")
            else:
                print("Prime")
        except EOFError:
            break


main()