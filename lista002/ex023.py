def ComoVaiSuaSaude(peso, sexo, altura):
    imc = peso / (altura ** 2)
   
    if sexo == "M":
        pi = (72.7 * altura) - 58
    elif sexo == "F":
        pi = (62.1 * altura) - 44.7
    else:
        return "Sexo inválido. Use 'M' ou 'F'."
    
    dif_percentual = abs(peso - pi) / pi * 100

    if imc < 18.5:
        imc_categoria = "abaixo"
    elif imc < 25:
        imc_categoria = "normal"
    elif imc < 30:
        imc_categoria = "acima"
    else:
        imc_categoria = "obeso"

    if dif_percentual <= 5 and imc_categoria == "normal":
        return "Você tem uma saúde ótima!"
    elif dif_percentual <= 10 and imc_categoria == "normal":
        return "Você tem uma saúde boa."
    elif peso < pi and imc_categoria == "abaixo":
        return "Atenção: Fique atento ao baixo peso!"
    elif dif_percentual > 10 and imc_categoria == "acima":
        return "Cuidado: Medidas acima do padrão!"
    elif dif_percentual > 10 and imc_categoria == "obeso":
        return "Procure Ajuda: Excesso de medidas!"
    else:
        return "Sem apontamento."