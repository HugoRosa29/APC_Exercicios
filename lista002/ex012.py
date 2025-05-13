def jogadas(a, b):
    diferenca = abs(b - a)
    movimentos = diferenca // 10
    if diferenca % 10 != 0:
        movimentos += 1
    print(movimentos)