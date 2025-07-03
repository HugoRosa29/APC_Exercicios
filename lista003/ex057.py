X = input().strip()
Y = input().strip()

distancia = 0
for i in range(len(X)):
    if X[i] != Y[i]:
        distancia += 1

print(distancia)