qtd = int(input())

for c in range(0, qtd):
    n1, n2, n3 = map(float, input().split())
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print(f"O ALUNO {c} FOI APROVADO")
    else:
        print(f"O ALUNO {c} FOI REPROVADO")