entrada = input().strip()
vogais = "aeiou"

for x in vogais:
    nova = ""
    for c in entrada:
        if c in vogais:
            nova += x
        else:
            nova += c
    print(nova)