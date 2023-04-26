#Aula 06 - Exercício 09

import os, math
os.system('cls' or 'clear')

num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
print('[1] Média')
print('[2] Diferença maior-menor')
print('[3] Produto')
print('[4] Divisão n1/n2')
option = int(input('Digite uma opção: '))

if option == 1:
    resultado = (num1+num2)/2
    print(f'A média é: {resultado}')
elif option == 2:
    if (num1 > num2):
        resultado = num1-num2
        print(f'A diferença é: {resultado}')
    else:
        resultado = num2 - num1
        print(f'A diferença é: {resultado}')
elif option == 3:
    resultado = num1 * num2
    print(f'A Produto é: {resultado}')
elif option == 4:
    if (num1 or num2 == 0):
        print('Impossivel dividir por zero!')
    else:
        resultado = num1 / num2
        print(f'A Divisão é: {resultado}')
else:
    print('Selecione uma das opções!!')
