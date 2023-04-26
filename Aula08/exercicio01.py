#Aula 08 - Exercício 01

import os, math
os.system('cls' or 'clear')

carneiro = 0

print('Entrada:')

while True:
    os.system('cls' or 'clear')
    dormir = input('Já dormiu? (s/n): ')

    if dormir == 'N' or dormir == "n":
        carneiro = carneiro + 1
    elif dormir == 'S' or dormir == "s":
        print('Saida:')
        print(f'Você contou {carneiro} carneirinhos!')
    else:
        break
