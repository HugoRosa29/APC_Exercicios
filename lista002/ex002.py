def area(a, b, forma=''):
    losango = int((a * b) / 2)
    if forma == 'losango':
        print(f'O losango tem {losango} de area')
    elif forma == 'triangulo':
        print(f'O triangulo tem {int((a * b) / 2)} de area')
    else:
        print(f'O retangulo tem {(a * b)} de area')
