def main():
    distancias = []
    intervalos = int(input())
    while intervalos > 0:
        intervalos -= 1
        x, y = input().split(" ")
        x, y = int(x), int(y)
        distancias.append(x * y)
    print(sum(distancias))

main()