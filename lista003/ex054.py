palavra = input()
vogais = "aoyeuiAOYEUI"
resultado = ""

for letra in palavra:
    if letra not in vogais:
        resultado += "." + letra.lower()

print(resultado)