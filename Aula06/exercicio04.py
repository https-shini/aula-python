#Aula 06 - Exercício 04

import os
os.system('cls' or 'clear')

h = float(input('Digite sua altura em metros: '))
print('Digite o seu sexo, M ou F: ')
sexo = input('Digite o seu genêro: ')
pesom = (72.7*h) - 58
pesof =  (62.1*h) - 44.7

if sexo == 'M' or sexo == 'm':
    print(f'O seu peso ideal é: {pesom}')
elif sexo == 'F' or sexo == 'f':
    print(f'O seu peso ideal é: {pesof}')
else:
    print('Seu genêro é invalido')
