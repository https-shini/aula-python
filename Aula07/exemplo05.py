#Aula 07 - Exemplo 05

import os
os.system('cls' or 'clear')

num = int(input('Digite um numero decimal: '))
binario =''
temp = num
while num > 0:
    binario = str(num%2) + binario
    num = num//2

print(f'O decimal {temp} é igual ao binário {binario}')
