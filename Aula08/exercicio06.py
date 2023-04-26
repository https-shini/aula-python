#Aula 08 - Exercício 06

import os, math
os.system('cls' or 'clear')

print('Entrada:')
valor_hora = float(input('Digite valor da hora aula: '))
carga = int(input('Digite a carga horária semanal: '))

salario_base = valor_hora * carga * 4.5
adicional = salario_base * 1/6
salario_final = salario_base + adicional

print('Saida')
print(f'Sálario final: R${salario_final}')
