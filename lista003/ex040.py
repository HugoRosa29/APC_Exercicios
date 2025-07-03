def validacao_senha(senha):
    if not (6 <= len(senha) <= 32):
        return "Senha invalida."
    if not all(c.isascii() and c.isalnum() for c in senha):
        return "Senha invalida."
    if not any(c.islower() for c in senha):
        return "Senha invalida."
    if not any(c.isupper() for c in senha):
        return "Senha invalida."
    if not any(c.isdigit() for c in senha):
        return "Senha invalida."
    return "Senha valida."

senha = input()
caracteres = list(senha)
print(validacao_senha(caracteres))
    