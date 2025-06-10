lista = list(map(int, input().split()))
repetidos = []
for ele in lista:
    if ele not in repetidos:
        repetidos.append(ele)

if len(repetidos) < len(lista):
    print(True)
else:
    print(False)