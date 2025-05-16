conflito = int(input())
criminalidade = float(input())
cond_saude = int(input())
alerta_viagem = int(input())
infra = int(input())

if criminalidade > 50:
    criminalidade = 1
else:
    criminalidade = 0
    
soma = criminalidade + conflito + cond_saude + alerta_viagem + infra

if soma == 5 or soma == 4:
    print("VIAGEM DESACONSELHADA")
elif soma == 3 or soma == 2:
    print("VIAGEM COM PRECAUCOES")
elif soma == 1:
    print("VIAGEM COM CUIDADOS")
else:
    print("VIAGEM SEGURA")