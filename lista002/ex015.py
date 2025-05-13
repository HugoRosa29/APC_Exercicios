def piscininha(x, y, w, h, a, b):
    if x < a < x + w and y < b < y + h:
        print("Dando um tchibum")
    elif (x <= a <= x + w and (b == y or b == y + h)) or (y <= b <= y + h and (a == x or a == x + w)):
        print("So com os pezin dentro da agua")
    else:
        print("Tomando um solzin")