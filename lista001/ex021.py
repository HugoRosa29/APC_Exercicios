pao = float(input())
bolo = float(input())
leite = float(input())
pago = float(input())
total = (pao * 0.5) + (bolo * 5) + (leite * 4.5)
troco = pago - total
print(f'Total: R${total:.2f}')
print(f'Troco: R${troco:.2f}')