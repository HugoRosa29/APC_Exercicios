def menor(n, s):
    for i in range(n - 1):
        if s[i] > s[i + 1]:
            return s[:i] + s[1+i:]
    return s[:-1]
    
n = int(input())
s = input()

print(menor(n, s))