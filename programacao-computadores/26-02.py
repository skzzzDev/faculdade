# criar um script que capture 2 números e realize as operações aritméticas com eles

numero1 = float(input('Digite o número 1:'))
numero2 = float(input('Digite o número 2:'))

media = (numero1 + numero2 ) / 2

#media
print(f'A média dos números é {media: .1f}')

#soma
print(f'A soma do numero 1 com o numero 2 é: { numero1 + numero2}')

#subtracao
print(f'A subtracao do numero 1 com o numero 2 é: { numero1 - numero2}')

#multiplicacao
print(f'A multiplicacao do numero 1 com o numero 2 é: { numero1 * numero2}')

#divisao
print(f'A divisao do numero 1 com o numero 2 é: { numero1 / numero2 }')

#resto
print(f'O resto do numero 1 com o numero2 é: { numero1 % numero2}')