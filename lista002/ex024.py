a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and c + b > a:
    if a != b and a != c and c!= b:
        print("ESCALENO")
    elif a == b == c:
        print("EQUILATERO")
    else:
        print("ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")