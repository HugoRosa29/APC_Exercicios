n = int(input())
tempos = list(map(int, input().split()))
tmax = max(tempos)

dif = []
for t in tempos:
    dif.append(tmax - t)

for ele in dif:
    print(ele, end=' ')
