def validarSenha(s):
    if len(s) < 8:
        return "Senha inválida, muito curta."

    temNumero = False 
    temMaiuscula = False

    for c in s:
        if c== " ":
            return "Senha invalida, não pode ter espaços"
        if c >= "0" and c <= "9":
            temNumero = True
        if c >= "A" and c <= "Z":
            temMaiuscula = True
    

    if temNumero == False:
        return "Senha inválida, precisa de um num. pelo menos"
    if not temMaiuscula:
        return "Senha inválida, precisa ser letra maisuscula"
    return "Senha válida"   

senha = input("Digite a senha: ") 
r = validarSenha(senha)
print(r)