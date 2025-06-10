lista = input().split()
pa = int(lista[0])
pb = int(lista[1])
t1 = float(lista[2])
t2 = float(lista[3])

if pa >= pb:
    print("A nunca alcancara B.")
elif t1 <= t2:
    print("A nunca alcancara B.")
else:
    anos = 0
    while pa < pb:
        pa = int(pa * (1 + t1 / 100))
        pb = int(pb * (1 + t2 / 100))
        anos += 1
        if anos > 1000:
            print("Mais de um milenio.")
            break
    else:
        print(f"Vai alcancar em {anos} ano(s).")