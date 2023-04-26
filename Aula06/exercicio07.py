#Aula 06 - Exercício 07

import os, math
os.system('cls' or 'clear')

print('Digite o valor das condernadas P(x, y)')
x = int(input('Digite o valor da cordenada X:'))
y = int(input('Digite o valor da cordenada Y:'))

if (x > 0 and y > 0):
    print(f'O ponto P ({x},{y}) pertence ao 1º Quadrante')
elif (x < 0 and y > 0):
    print(f'O ponto P ({x},{y}) pertence ao 2º Quadrante')
elif (x < 0 and y < 0):
    print(f'O ponto P ({x},{y}) pertence ao 3º Quadrante')
elif (x > 0 and y < 0):
    print(f'O ponto P ({x},{y}) pertence ao 4º Quadrante')
