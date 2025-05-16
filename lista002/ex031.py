angulo = int(input())

if 0 < angulo < 90:
    print("AGUDO")
elif angulo == 90:
    print("RETO")
elif 90 < angulo < 180:
    print("OBTUSO")
elif angulo == 180:
    print("RASO")
elif 180 < angulo < 360:
    print("CONCAVO")
elif angulo == 360:
    print("COMPLETO")
else:
    print("ANGULO INVALIDO")