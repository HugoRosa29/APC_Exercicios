n = int(input())
x = 0
for _ in range(n):
    linha = input()
    if '++' in linha:
        x += 1
    elif '--' in linha:
        x -= 1
print(x)