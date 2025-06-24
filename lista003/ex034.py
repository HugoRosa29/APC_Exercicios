lista = list(map(int, input().split()))
soma = 0
for ele in lista:
    print(ele + soma, end=' ')
    soma += ele

for c, v in enumerate(lista):
    if c == 0:
        print(f"\n{v}", end=' ')
    else:
        print(v, end=' ')