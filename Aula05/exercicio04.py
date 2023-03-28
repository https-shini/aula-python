#Exercicio 04

import os
os.system('cls' or 'clear')

conta_h20 = float(input('Digite o valor da conta de água: '))
conta_luz = float(input('Digite o valor da conta de luz: '))
conta_cell = float(input('Digite o valor da conta de celular: '))

salario = float(input('Digite o seu salário R$: '))
contas = conta_cell+conta_h20+conta_luz

if salario >= contas:
    print(f'Restou R$ {salario - contas} do seu salário')
else:
    print(f'Voce não tem saldo o suficente para pagar as suas contas')
