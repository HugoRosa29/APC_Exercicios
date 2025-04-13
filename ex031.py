lista = input().split(':')
hora = int(lista[0])
minuto = int(lista[1])
segundo = int(lista[2])
tots = (hora * 3600) + (minuto * 60) + segundo
print(f'La se foram {tots} segundos que nao voltam mais...')