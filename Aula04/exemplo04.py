#Exemlo 2 - Aula 04

import os
os.system('cls' or 'clear')

num = int(input('Digite um numero: '))

if num%2 == 0:
    print('O numero é par.')


resposta = "par" if num%2 == 0 else 'impar'
print(f'O numero {num} é {resposta}')