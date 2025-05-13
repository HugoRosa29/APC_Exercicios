def qualPeriodo(m, a, s):
    prefixo = str(m)[:4]

    ano_ingresso = 2000 + int(prefixo[:2])
    semestre_ingresso = int(prefixo[3])

    semestre_total_ingresso = ano_ingresso * 2 + semestre_ingresso
    semestre_total_atual = a * 2 + s

    res = semestre_total_atual - semestre_total_ingresso + 1
    print(res)