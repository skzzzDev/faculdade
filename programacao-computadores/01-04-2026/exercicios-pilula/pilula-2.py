def simularCrescimento(pop, taxa, limite): 
    anos = 0

    while pop <= limite:
        pop = pop * ( 1 + taxa / 100 )
        anos += 1
    return anos


p = float(input("População: "))
t = float(input(" Taxa (%): "))
l = float(input(" limite : "))
print(f"Anos = {simularCrescimento(p,t,l)}")