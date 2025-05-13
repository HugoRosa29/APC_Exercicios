def classificador(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('triangulo')
        if a == b or a == c or b == c:
            print('isosceles') 
        if a == b == c:
            print('equilatero')
          
        if a != b and a != c and c != b:
            print('escaleno')
        if a ** 2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == a**2+b**2:
            print("retangulo") 
    else:   
        print('gondim sendo gondim')
