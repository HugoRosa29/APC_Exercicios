n_hab = int(input())
total = 0
for c in range(0, n_hab):
    qtd_dinheiro = int(input())
    if qtd_dinheiro < 1000:
        doacao = 1000 - qtd_dinheiro
        total += doacao
print(total)