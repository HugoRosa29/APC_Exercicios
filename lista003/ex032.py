def remove_duplicatas(lista):
    lista2 = []
    for ele in lista:
        if ele not in lista2:
            lista2.append(ele)
    return lista2
    
