num = int(input())
i = 0

if num > 50:
    num = 0

print(f"N[0] = {num}")

while i < 9:
    i = i + 1
    num = num * 2
    print(f"N[{i}] = {num}")