tot = float(input())
atual = float(input())
meses = float(input())
falta = tot - atual
economia = falta / meses
print(f'Voce precisa economizar R${economia:.2f} por mes')