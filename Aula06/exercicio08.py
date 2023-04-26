#Aula 06 - Exercício 08

import os, math
os.system('cls' or 'clear')

nome = input('Digite o seu nome: ')
hora = float(input('Digite que horas são [0-23]: '))

if (hora >= 5 and hora <= 12):
    print(f'Bom dia, {nome}')
elif (hora >= 13 and hora <= 18):
    print(f'Boa tarde, {nome}')
elif (hora >= 19 and hora <= 4):
    print(f'Boa noite, {nome}')
