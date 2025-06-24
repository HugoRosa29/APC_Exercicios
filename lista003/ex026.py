numeros = list(map(int, input().split()))
num = 0
pontuação = []
for i in numeros:
    while True:
        num = i
        if num < 0:
            break
        pontuação.append(num)
        break

pontuação.reverse()
print(*pontuação)
