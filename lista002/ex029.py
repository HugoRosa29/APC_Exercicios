vel = int(input())

if vel <= 50:
    print("SEM INFRACAO")
elif 51 <= vel <= 80:
    print("INFRACAO LEVE")
elif 81 <= vel <= 120:
    print("INFRACAO GRAVE")
else:
    print("INFRACAO GRAVISSIMA")