#Exemlo 1 - Aula 04

import os
os.system('cls' or 'clear')

idade = float(input('Digite asua idade: '))

resposta = "Parabens você pode ter CNH" if idade>=18 else 'Parabens voce pode peir uber!!'
print(f'Sua idade é {idade}, {resposta}')
