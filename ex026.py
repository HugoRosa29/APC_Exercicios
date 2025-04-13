conta = float(input())
por = int(input())
gorjeta = conta * (por / 100)
tot = conta + gorjeta
print(f'Valor da gorjeta: R${gorjeta:.2f}')
print(f'Valor total: R${tot:.2f}')