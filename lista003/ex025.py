lista = list(map(int, input().split()))
print(f'{min(lista)} {lista.index(min(lista))}')
print(f'{max(lista)} {lista.index(max(lista))}')
for c in lista:
    print(c, end=" ")