n_pro = int(input())
problemas_res = 0

for c in range(n_pro):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        problemas_res += 1
    
print(problemas_res)
