#Aula 07 - Exemplo 04

import os
os.system('cls' or 'clear')

n = 1
while n<11:
    nome = input('Digite o nome do aluno: ')
    nota01 = float(input(f'Digite a 1º nota do {nome} '))
    nota02 = float(input(f'Digite a 2º nota do {nome} '))
    media = (nota01 + nota02)/2
    print(f'A média do aluno {nome} é de {media: .2f}')
    n = n+1
