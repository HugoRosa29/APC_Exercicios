s = input()
n = len(s)

diferencas = 0
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        diferencas += 1

if diferencas == 0 and n % 2 == 1:
    print("ON")
elif diferencas == 1:
    print("ON")
else:
    print("OFF")