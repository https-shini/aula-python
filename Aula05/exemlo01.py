#Exemlo 01

import os
os.system('cls' or 'clear')

frequencia = float(input('Digite a sua frequencia: '))
media = float(input('Digite a média das suas notas: '))

if frequencia < 75:
    print('Voce foi reprovado pela sua frequencia')
elif frequencia >= 75 and media < 6:
    print('Voce foi reprovado pela sua média')
elif frequencia >= 75 and media >= 6:
    print('Voce foi aprovado')
