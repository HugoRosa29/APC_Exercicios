def maior_norma(lista1, lista2):
    norma1 = norma2 = 0
    for ele in lista1:
        norma1 += abs(ele)
    for ele in lista2:
        norma2 += abs(ele)
        
    if norma1 > norma2:
        print("PRIMEIRO")
    else:
        print("SEGUNDO")