altura = float(input())
sexo = input()

if sexo == 'M':
    pi = (72.7 * altura) - 58
    print(f"{pi:.2f}")
else:
    pi = (62.1 * altura) - 44.7
    print(f"{pi:.2f}")