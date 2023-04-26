#Aula 08 - Exercício 04

import os, math
os.system('cls' or 'clear')

soma = 0
print('Entrada:')
num = input('Digite o número da conta em 4 algarismos: ')

for c in num:
    soma = soma + int(c)

digito = soma%10

print('Saida:')
print(f'O número da conta competo é {num}-{digito}')
