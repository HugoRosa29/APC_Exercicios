def imprimeJogo(matriz):
    for linha in matriz:
        print("".join(linha))
    
def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz