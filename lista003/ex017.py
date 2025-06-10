n = int(input())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

soma = 0
for i in range(n):
    soma += u[i] * v[i]

if soma == 0:
    print("ortogonais")
else:
    print(soma)
