def eh_primo(n):
    if n <= 1:
        return "regular"
    if n == 2:
        return "primo"
    if n % 2 == 0:
        return "regular"
    i = 3
    while i * i <= n:
        if n % i == 0:
            return "regular"
        i += 2
    return "primo"

num = int(input())
print(eh_primo(num))
    