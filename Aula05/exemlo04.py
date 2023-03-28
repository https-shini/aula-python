#Exemlo 04

import os
os.system('cls' or 'clear')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura**2

if imc <20:
    print('Voce esta abaixo do peso')
elif imc <25:
    print('Voce esta com o peso normal')
elif imc <30:
    print('Voce esta com sobrepeso')
elif imc <40:
    print('Voce esta obeso')
else:
    print('Voce esta muito gigante!')
