#Exemlo 5 - Aula 04

import os
os.system('cls' or 'clear')

nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua nota: '))

media = (nota1 + nota2) / 2

print('A sua média foi: ', media)

if media>=6.0:
    print('Voce foi aprovado')

else:
    print("Voce foi reprovado")
