def pacotesDeBolacha(m, n, k):
    pacotes_por_aluno = min(k, m // n)
    total_distribuidos = pacotes_por_aluno * n
    print(total_distribuidos)