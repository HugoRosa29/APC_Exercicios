def age(dia):
    ano = dia // 360
    meses = (dia % 360) // 30
    diares = (dia % 360) % 30
    print(f"{ano} ano(s), {meses} mes(es) e {diares} dia(s)")
    
    
lista = input().split()
age(int(lista[0]))
age(int(lista[1]))
age(int(lista[2]))