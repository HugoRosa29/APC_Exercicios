def descomprimir(s):
    resultado = ''
    i = 0
    while i < len(s):
        letra = s[i]
        i += 1
        numero = ''
        while i < len(s) and s[i].isdigit():
            numero += s[i]
            i += 1
        resultado += letra * int(numero)
    return resultado


n = int(input())
for _ in range(n):
    linha = input().strip()
    print(descomprimir(linha))