#Exemlo 7 - Aula 04

import os
os.system('cls' or 'clear')

num = int(input('Digite um numero: '))

resposta = "par" if num%2 == 0 else 'impar'
print(f'O numero {num} é {resposta}')
