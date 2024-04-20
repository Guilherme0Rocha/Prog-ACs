arr = []
num = int(input())
lista = list(map(int, input().split()))

for i in range(num):
    arr.insert(i,lista[i])

print("Menor valor: %d" % (min(arr)))

for i in range(num):
    if arr[i] == min(arr):
        pos = i

print("Posicao: %d" % pos)