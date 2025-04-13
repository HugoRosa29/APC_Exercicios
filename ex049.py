def age(dia):
    ano = dia // 360
    meses = (dia % 360) // 30
    diasres = (dia % 360) % 30
    print(f"{ano} {meses} {diasres}")


lista = input().split()
age(int(lista[0]))
age(int(lista[1]))
age(int(lista[2]))