def formamisteriosa(a, b, c):
    if a == b:
        print('pode ser quadrado')
    else:
        print('pode ser retangulo')
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print('pode ser triangulo equilatero')
        elif a == b or a == c or b == c:
            print('pode ser triangulo isosceles')   
        elif a != b and a != c and c != b:
            print('pode ser triangulo escaleno')