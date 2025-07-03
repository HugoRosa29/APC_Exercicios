n = int(input())

for _ in range(n):
    palavra = input()
    if len(palavra) > 10:
        abreviada = palavra[0] + str(len(palavra) - 2) + palavra[-1]
        print(abreviada)
    else:
        print(palavra)