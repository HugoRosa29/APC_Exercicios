num = cont = soma = 0
while True:
    num = int(input())
    if num == -1:
        break
    soma += (1 / num)
    cont += 1
media = cont / (soma)
print(int(media))