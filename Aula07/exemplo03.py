#Aula 07 - Exemplo 03

import os
os.system('cls' or 'clear')

binario = input('Digite um númeo: ')

n = len(binario) - 1
decimal = 0

for d in binario:
    decimal = decimal + d * 2**n
    n = n-1

print(f'O binário {binario} é igual a {decimal} na base 10')
