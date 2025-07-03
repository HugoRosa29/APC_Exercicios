def contar_navios(s):
    contador = 0
    i = 0
    while i < len(s):
        if s[i] == 'o':
            contador += 1
            while i < len(s) and s[i] == 'o':
                i += 1
        else:
            i += 1
            
    return contador
    

s = input().strip()
print(contar_navios(s))