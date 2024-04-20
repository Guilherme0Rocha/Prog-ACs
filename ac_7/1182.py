col = int(input())
op = input()

m = []
for i in range(12):
    m.append([])

for i in range(12):
    for j in range(12):
        x = float(input())
        m[i].append(x)

if op == 'S':
    soma = 0
    for k in range(12):
        soma += m[k][col]
    print('{:.1f}'.format(soma))
elif op == 'M':
    media = 0
    soma = 0
    for k in range(12):
        soma += m[k][col]
    media = soma / 12
    print('{:.1f}'.format(media))
