def ritmoMedio(h, m, s, d):
    totalseg = h * 3600 + m * 60 + s
    ritmoseg = totalseg / d
    minutos = int(ritmoseg // 60)
    segundos = int(ritmoseg % 60)
    if segundos == 60:
        minutos += 1
        segundos = 0
    print(f"{minutos:02d}:{segundos:02d} min/km")