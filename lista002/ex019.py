def EhBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return "Bissexto"
    else:
        return "Ano Comum"