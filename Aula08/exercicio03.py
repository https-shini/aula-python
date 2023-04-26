#Aula 08 - Exercício 03

import os, math
os.system('cls' or 'clear')

print('Entrada:')

num = 0
soma = 0
neleitor = 0
for a in range(10):
    idade = int(input(f'Digite a idade do {a+1}º aluno: '))
    if idade >= 16:
        num = num + 1
    else:
        neleitor = neleitor + 1
        soma = soma + idade

media = soma / neleitor

print(f'A quantidade de alunos que podem votar é de {num}')
print(f'A média de idade dos alunos não eleitores são {media}')
