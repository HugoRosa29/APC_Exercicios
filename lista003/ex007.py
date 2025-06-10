num = int(input())

is_negative = False
if num < 0:
    is_negative = True
    num = abs(num)

lista_num = list(str(num))
lista_num.reverse()

string_reversa = "".join(lista_num)
inteiro_reverso = int(string_reversa)

if is_negative:
    inteiro_reverso = -inteiro_reverso

print(inteiro_reverso)