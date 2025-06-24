def soma_aninhada(lista):
    total = 0
    for i in lista:
        if isinstance(i, list):
            total += soma_aninhada(i)
        else:
            total += i
    return total