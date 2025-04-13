def maiorAB(a, b):
    if a > b:
        print(a)
    else:
        print(b)


for c in range(0, 5):
    lista = input().split()
    maiorAB(int(lista[0]), int(lista[1]))
    lista.clear()

