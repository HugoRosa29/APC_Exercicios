def print_rectangle(a):
    print(a)
    b = 'x'
    c = ' '
    print(f'{b * a}')
    print(f'x{c * (a-2)}x')
    print(f'x{c * (a-2)}x')
    print(f'{b * a}')


lista = input().split()
for c in range(0, 3):
    a = int(lista[c])
    print_rectangle(a)
    c += 1