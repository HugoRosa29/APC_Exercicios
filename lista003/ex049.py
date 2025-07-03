n = int(input())
s = input()

if n % 4 != 0:
    print("Feiticeiro misterioso")
else:
    a = c = g = t = q = 0

    for ch in s:
        if ch == 'A':
            a += 1
        elif ch == 'C':
            c += 1
        elif ch == 'G':
            g += 1
        elif ch == 'T':
            t += 1
        elif ch == '?':
            q += 1

    alvo = n // 4

    falta_a = alvo - a
    falta_c = alvo - c
    falta_g = alvo - g
    falta_t = alvo - t

    total_faltando = falta_a + falta_c + falta_g + falta_t

    if falta_a < 0 or falta_c < 0 or falta_g < 0 or falta_t < 0:
        print("Feiticeiro misterioso")
    elif q == total_faltando:
        print("Segredos desvendados")
    else:
        print("Feiticeiro misterioso")