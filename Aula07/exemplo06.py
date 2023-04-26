#Aula 07 - Exemplo 06

import os
os.system('cls' or 'clear')

resp = 's'
soma = 0
qte = 0

while resp == 's' or resp == 'S':
    num = int(input('Digite um número ou 0 para sair: '))
    soma = soma + num
    if num == 0:
        break
    qte = qte + 1

media = soma/qte
print(f'A média é {media:.2f}')
