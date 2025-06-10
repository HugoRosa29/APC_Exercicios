seq = list(map(int, input().split()))
inversoes = 0

for i in range(len(seq)):
    for j in range(i + 1, len(seq)):
        if seq[i] > seq[j]:
            inversoes += 1

print(inversoes)