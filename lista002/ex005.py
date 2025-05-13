def dinheiros(n, a, b):
    if b <= a:
        qnt_b = int(n/2)
        qnt_a = n % 2
        tot = qnt_b * b + qnt_a * a
        print(tot)
    else:
        tot = n * a
        print(tot)