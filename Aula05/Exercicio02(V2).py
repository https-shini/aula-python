#Exercicio 02 - V2

import os
os.system('cls' or 'clear')

turno = input('Digite o seu turno de trabalho (N ou D): ')
horas = int(input('Digite a quantidade de horas trabalhadas: '))

if turno == 'N' or turno == 'n':
    valor_hora = 45
elif turno == 'D' or turno == 'd':
        valor_hora = 37.50
elif turno == 'E' or turno == 'e':
        valor_hora = 50    
else:
    print('Opção invalida!!!!!!')

salario = horas * valor_hora
print(f'o salario de é R$ {salario}')
