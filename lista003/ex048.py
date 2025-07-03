s = input()

corinthians = '0000000' in s
saopaulo = '1111111' in s

if corinthians and saopaulo:
    print("JOGO PESADO")
elif corinthians:
    print("VAI TIMAO")
elif saopaulo:
    print("VAMO TRICOLOR")
else:
    print("BORA UM VIRTUAL NO CODEFORCES")