def menu():
    while True:
        print("1 - Soma")
        print("2 - Média")
        print("3 - Sair" )
        opc = int(input("Opção: "))
        if opc == 3:
           break
        n1 = float(input("N1 "))
        n2 = float(input("N2 "))
        if opc == 1:
           print(f"Some é {n1+n2}")
        elif opc ==2:
           print(f"Média é {n1+n2/2}")
        else:
           print
           ("Opção invalida")