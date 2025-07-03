'''Cada posição da lista desenho representa um dos estados da forca'''
desenhos = ['''
 +---+
 |   |
     |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
     |
     |
     |
========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========''']

palavra = input("Digite a palavra secreta: ").lower()
letras = list(palavra)
letras_corretas = ["_"] * len(letras) 
qtd_erros = 0
max_erros = 6
while True:
     print(desenhos[qtd_erros])
     print()
     print(" ".join(letras_corretas))
     
     if "_" not in letras_corretas:
         print(f'Sim! A palavra secreta eh "{palavra}"')
         break
         

     res_usu = input("Digite uma letra: ")
     if res_usu not in letras:
          qtd_erros += 1
          if qtd_erros >= 6:
              print(desenhos[qtd_erros])
              print()
              print(" ".join(letras_corretas))
              print("Voce teve muitas oportunidades e perdeu!")
              break
     else:
          for i in range(len(letras)):
              if letras[i] == res_usu:
                  letras_corretas[i] = res_usu