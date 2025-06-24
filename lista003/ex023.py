n = int(input())
habilidades = list(map(int, input().split()))

habilidades.sort(reverse=True)

max_diferenca = 0
max_reservas = min(11, n - 11)

for k in range(1, max_reservas + 1):
    t = sum(habilidades[:11])         
    r = sum(habilidades[11:22])
    diferenca = abs(t - r)
    if diferenca > max_diferenca:
        max_diferenca = diferenca

print(max_diferenca)