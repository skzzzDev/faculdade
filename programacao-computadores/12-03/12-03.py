import os
import math

os.system('cls')

# cima = math.ceil(6.4)
# baixo = math.floor(6.5)
# raiz = math.sqrt(81)

print('Equação de segundo grau')
a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

print(f'{a}x2 + {b}x + {c} = 0')

delta = b * b - 4 * a * c

x1 = (-b + delta ** 0.5) / (2*a)
x2 = (-b - delta ** 0.5) / (2*a)

print(f'x1 {x1} = {x2}')

print('Exercício 1 >')
num = int(input('Digite o numero inteiro: '))
d1 = num // 100
d2 =  ( num // 10 ) % 10
d3 = num % 10

invert = d3 * 100 + d2 * 10 + d1

print(f'{invert}')

print('Exercício 2 >')
raizNum = float(input('Digite um número para encontrar a raiz quadrada: '))
resultRaiz = math.sqrt(raizNum)
print(f'A raiz do número {raizNum} digitado é {resultRaiz: .2f}!')


print('Exercício 3 >')
num = int(input('Digite um número: '))
absolute = math.fabs(num)
inteiroNum = math.trunc(num)
raziNum = math.sqrt(num)
fatorialNum = math.factorial(num)


print(f' Número Absoluto: {absolute} \n Número Inteiro: {inteiroNum} \n Raiz do número: {raziNum} \n Número Fatorial: {fatorialNum}')

print('Exercício 4 >')
raio = float(input('Digite o raio do circulo: '))
area = math.pi * (raio ** 2)
circuferencia = 2 * math.pi * raio

print(f'Área do circulo: {area: .2f}')
print(f'Circufeencia: {circuferencia: .2f}')

print('Exercício 5')
capital = float(input('Digite a capital: '))
juros = int(input('Digite o juros: '))
periodo = int(input('Digite o periodo: '))
taxa = juros / 100

montante = capital * ( 1 + taxa ) ** periodo

print(f'Valor do juros: {montante: .2f}')