pares = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        pares = pares + 1

print(f"{pares} valores pares")