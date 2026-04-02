def contarNotas(valor):
    for nota in (100, 50, 10 ):
        qtd = valor // nota
        valor = valor % nota 
        
        if qtd > 0 : 
            print(f"{qtd} nota(s) de R$ {nota} ")


valor = float(input("Qual valor: "))
contarNotas(valor)