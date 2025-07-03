def decompress(x: int) -> str:
    letras = []
    while x > 0:
        valor = x & 31
        letras.append(chr(64 + valor))
        x >>= 5
    return "".join(letras)