lista = input().split()
num_amigos = int(lista[0])
preco_ingre = int(lista[1])
soma = 0

for c in range(0, num_amigos):
    din = int(input())
    soma += din
media = soma / num_amigos
print(f'media: {int(media)}')
if media < preco_ingre:
    print("rockeiros trabalhando ja")
else:
    print("o rock reinara mais uma vez")