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