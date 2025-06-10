total = int(input())
compradas = int(input())
lista = []

for c in range(0, compradas):
    num_figurinha = int(input())
    if num_figurinha not in lista:
        lista.append(num_figurinha)
        
res = total - len(lista)
print(res)