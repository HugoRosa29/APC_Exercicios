q = int(input())
for _ in range(q):
    entrada = input().split()
    l = int(entrada[0])
    r = int(entrada[1])
    s = entrada[2]
    substring = s[l:r+1]
    print(substring[::-1])