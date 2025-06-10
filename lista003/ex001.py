cot_dolar = float(input())
tam_lote = int(input())
qtd = int(input())
for c in range(0, qtd):
    print(f"Lote: {c+1} - Total da venda: R$ {(cot_dolar * tam_lote) * 1.025:.2f}")