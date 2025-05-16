lista = input().split()
x = int(lista[0])
y = int(lista[1])

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif x == 0 and y != 0:
    print("EIXO Y")
elif x != 0 and y == 0:
    print("EIXO X")
else:
    print("ORIGEM")