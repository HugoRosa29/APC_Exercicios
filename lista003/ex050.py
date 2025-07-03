palavra = input()
letras = list(palavra)
contmai = contmin = 0
for l in letras:
    if l.isupper():
        contmai += 1
    else:
        contmin += 1

if contmai > contmin:
    print(palavra.upper())
else:
    print(palavra.lower())
