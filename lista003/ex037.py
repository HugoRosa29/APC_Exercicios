def menor_qtd_zeros(strings):
    resultado = []
    for s in strings:
        if '1' not in s:
            resultado.append(0)
            continue
        comeco = s.find('1')
        final = s.rfind('1')
        zero_para_remover = s[comeco:final+1].count('0')
        resultado.append(zero_para_remover)
    return resultado
    
n = int(input())
strings = [input().strip() for _ in range(n)]
resultados = menor_qtd_zeros(strings)
for r in resultados:
    print(r)