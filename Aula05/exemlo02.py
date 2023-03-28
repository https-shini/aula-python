#Exemlo 02

import os
os.system('cls' or 'clear')

diaria = input('Digite o tipo de diaria desejada (S, D e T): ')
dias = int(input('Digite a quantidade de dias que deseja ser hospedado: '))

if diaria == 'S' or diaria == "s":
    print(f'O valor a pagar é: {dias * 255,50}')
elif diaria == 'D' or diaria == "d":
    print(f'O valor a pagar é: {dias * 305,50}')
elif diaria == 'T' or diaria == "t":
    print(f'O valor a pagar é: {dias * 360,50}')
else:
    print('Tipo de diaria inválido')
