#Aula 06 - Exercício 03

import os
os.system('cls' or 'clear')

num = int(input('Digite um número inteiro: '))

if num > 0:
    print(f' O número {num} é positivo')

elif num == 0:
    print(f' O número {num} é nulo')

elif num < 0:
    print(f' O número {num} é negativo')
