def main():
    while True:
        mary = 0
        john = 0
        num = int(input())
        if num == 0:
            break
        partidas = input().split(" ")
        for elemento in partidas:
            if elemento == "0":
                mary += 1
            elif elemento == "1":
                john += 1
        print(f"Mary won {mary} times and John won {john} times")
        pass

main()