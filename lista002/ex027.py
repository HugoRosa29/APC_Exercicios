renda = float(input())

if renda <= 1903.98:
    print("ISENTO")
elif 1903.99 <= renda <= 2826.65:
    imposto = renda * 0.075
    print(f"{imposto:.2f}")
elif 2826.66 <= renda <= 3751.05:
    imposto = renda * 0.15
    print(f"{imposto:.2f}")
elif 3751.06 <= renda <= 4664.68:
    imposto = renda * 0.225
    print(f"{imposto:.2f}")
else:
    imposto = renda * 0.275
    print(f"{imposto:.2f}")