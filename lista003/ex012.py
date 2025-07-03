num = 0
soma = cont = 0
while True:
    num = int(input())
    if num == -1:
        break
    soma += num
    cont += 1
    if num == -1:
        break
media = soma / cont
print(int(media))
    