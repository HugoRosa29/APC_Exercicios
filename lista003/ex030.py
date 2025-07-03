def imprimeJogo(matriz):
    for linha in matriz:
        print("".join(linha))
    
def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz
    
def jogoTerminou(matriz):
    for linha in matriz:
        if linha[0] == linha[1] == linha[2] and linha[0] != " - ":
            return 1
    
    for col in range(3):
        if matriz[0][col] == matriz[1][col] == matriz[2][col] and matriz[0][col] != " - ":
            return 1
    
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != ' - ':
        return 1
        
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != ' - ':
        return 1 
    
    for linha in matriz:
        if ' - ' in linha:
            return 0
    
    return 2
    

matriz = [[' - ', ' - ', ' - '], 
            [' - ', ' - ', ' - '], 
            [' - ', ' - ', ' - ']]
    
    
jogador = ' X '

while True:
    
    imprimeJogo(matriz)
    lin, col = map(int, input().split())
    
    if matriz[lin][col] == ' - ':
        matriz = atualizaMatriz(matriz, lin, col, jogador)
        
    estado = jogoTerminou(matriz)
    if estado == 1:
        imprimeJogo(matriz)
        print("Ganhou")
        break
    elif estado == 2:
        imprimeJogo(matriz)
        print("Empate")
        break
    
    jogador = ' O ' if jogador == ' X ' else ' X '