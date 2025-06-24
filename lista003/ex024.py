lista = list(map(int, input().split()))
soma = variancia = 0
for ele in lista:
    soma += ele

media = soma / len(lista)

for i in lista:
    variancia += (i - media) ** 2 / len(lista) 
desvio = variancia ** (1/2)
print(f'{variancia:.1f}')
print(f'{desvio:.1f}')