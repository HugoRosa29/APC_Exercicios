def Alfabeto(a):
    valor_ascii = ord(a)
    if valor_ascii == 65 or valor_ascii == 69 or valor_ascii == 73 or valor_ascii == 79 or valor_ascii == 85 or valor_ascii == 97 or valor_ascii == 101 or valor_ascii == 105 or valor_ascii == 111 or valor_ascii == 117:
        return "Vogal"
    else:
        return "Consoante"