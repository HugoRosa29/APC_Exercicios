def print_rectangle(a):
    print(a)
    b = '+'
    c = ' '
    print(f'{b * a}')
    print(f'+{c * (a-2)}+')
    print(f'{b * a}')


lista = input().split()
for c in range(0, 3):
    a = int(lista[c])
    print_rectangle(a)
    c += 1
    