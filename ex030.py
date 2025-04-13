lista = input().split('/')
dia = lista[0]
mes = lista[1]
ano = lista[2]
print(f'{dia}-{mes}-{ano}')
print(f'{mes}-{dia}-{ano}')
print(f'{ano}/{mes}/{dia}')