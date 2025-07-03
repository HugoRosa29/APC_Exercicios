num = int(input())

for i in range(num):
    jogada = input().split()
    jog01 = jogada[0]
    jog02 = jogada[1]
    if jog01 == jog02:
        print("Empate.")
    elif (jog01 == 'tesoura' and jog02 == 'papel') or (jog01 == 'papel' and jog02 == 'pedra') or (jog01 == 'pedra' and jog02 == 'tesoura'):
        print("Jogador 01 venceu.")
    else:
        print("Jogador 02 venceu.")
