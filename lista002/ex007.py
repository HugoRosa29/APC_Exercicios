def realidade(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        print('complexas')
    else:
        print('reais')