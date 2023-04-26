#Aula 07 - Exemplo 02

import os
os.system('cls' or 'clear')

soma = 0
for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    soma = soma + num

media = soma/10

print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
