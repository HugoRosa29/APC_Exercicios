frase = input()
saida = []

for i in range(len(frase)):
    c = frase[i]
    saida.append(c)
    if c != ' ' and i != len(frase) - 1 and frase[i + 1] != ' ':
        saida.append(' ')

print(''.join(saida))