[A, B, C]= input().split(" ")

A = int(A)
B = int(B)
C = int(C)

MaiorAB = int((A + B + abs(A - B))/2)

if MaiorAB < C:
    MaiorAB = C

print(MaiorAB, "eh o maior")