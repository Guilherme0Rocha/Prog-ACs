x = int(input())
y = int(input())
t = x

soma = 0

if x > y:
    x = y
    y = t

for i in range(x, y+1):
    if i % 13 != 0:
        soma = soma + i

print(soma)