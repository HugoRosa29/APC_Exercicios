idade = int(input())
if idade < 16:
    print("NAO PODE VOTAR")
elif 16 <= idade < 18 or idade >= 70:
    print("VOTO OPCIONAL")
elif 18 <= idade < 70:
    print("VOTO OBRIGATORIO")
