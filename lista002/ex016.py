def quantosJantam(n, g, f, c):
    pares = min(g, f)
    tot_pares = pares + c
    if tot_pares > n:
        print(n)
    else:
        print(tot_pares)