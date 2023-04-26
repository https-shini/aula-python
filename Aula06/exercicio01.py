#Aula 06 - Exercício 01

import os
os.system('cls' or 'clear')

salario = float(input('Digite o valor do seu salário fixo: '))
vendas = float(input('Digite o valor da suas vendas: '))

comissao = vendas * 1.04 - vendas
print(f'Sua comissão é de: {comissao}')

sfinal = salario + comissao
print(f'Sua salário final é de: {sfinal}')
