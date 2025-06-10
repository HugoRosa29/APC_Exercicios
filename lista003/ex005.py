k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

cont = 0
for c in range(1, d + 1):
    if c % k == 0 or c % l == 0 or c % m == 0 or c % n == 0:
        cont += 1
print(cont)