#Exercicio 02

import os
os.system('cls' or 'clear')

turno = input('Digite o seu turno de trabalho (N ou D): ')
horas = int(input('Digite a quantidade de horas trabalhadas: '))

if turno == 'N' or turno == 'n':
    valor_hora = 45
else:
    valor_hora = 37.50

salario = horas * valor_hora
print(f'o salario de é R$ {salario}')
