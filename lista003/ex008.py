def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

n1, n2 = map(int, input().split())
if calcular_mdc(n1, n2) == 1:
    print("Sao co-primos.")
else:
    print("Nao sao co-primos!")