n = int(input())
tempos = list(map(int, input().split()))
tmin = min(tempos)

dif = []
for t in tempos:
    dif.append(t - tmin)

for ele in dif:
    print(ele, end=' ')
