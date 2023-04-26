#Aula 08 - Exercício 05

import os, math
os.system('cls' or 'clear')

soma = 0

print('Entrada:')
turma = int(input('Digite a quatidade de turmas: '))

for i in range(turma):
    alunos = int(input(f'Digite a quatidade de alunos da {i + 1}º tuma: '))
    soma = soma + alunos

media = soma/turma

print(f'As turmas têm em média {media} alunos.')
