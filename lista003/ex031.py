num_sapato = int(input())
lista = list(map(int, input().split()))
lista.sort()
cont = 0

for pos, ele in enumerate(lista):
    if ele >= num_sapato:
        cont += 1
        print(pos)
        break
if cont == 0:
    print(-1)

