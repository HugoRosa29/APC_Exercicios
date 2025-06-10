qtd = int(input())
lista = []
for c in range(0, qtd):
    num = int(input())
    lista.append(num)
print(f'Menor: {min(lista)}')
print(f"Maior: {max(lista)}")