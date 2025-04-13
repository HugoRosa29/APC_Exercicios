def concatenar(a, b):
    return a + b
def repetir(a, b):
    return a * b

lista = input().split()
print(concatenar(lista[0], lista[1]))
print(repetir(lista[0], int(lista[2])))
print(repetir(concatenar(lista[0], lista[1]), int(lista[2])))
