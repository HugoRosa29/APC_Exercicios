def qtdcopos(n):
    if n <= 0:
        print("Pode voltar pro ceubinho, deivis! Falta(m) 4 copo(s)!")
    else:
        tot = n % 4 
        if tot == 0:
            print("Pode levar pros calourinhos, deivis!")
        else:
            print(f"Pode voltar pro ceubinho, deivis! Falta(m) {4 - tot} copo(s)!")