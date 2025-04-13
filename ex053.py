def qualPeriodo(m, a, s):
    prefixo = int(str(m)[:4])
    comeco = 2000 + int(str(prefixo)[:2])
    semestreini = int(str(prefixo)[3])
    totsemingre= comeco * 2 + semestreini
    semestretot = a * 2 + s

    res = semestretot - totsemingre + 1
    print(res)