#Aula 06 - Exercício 06

import os, math
os.system('cls' or 'clear')

nota1 = float(input('Digite a sua primeira nota parcial: '))
nota2 = float(input('Digite a sua segunda nota parcial: '))
media = (nota1 + nota2)/2

if media >= 9:
    print('Coneito A, parabéns você foi aprovado!')
elif (media >= 7.5 and media <= 8.9):
    print('Coneito B, parabéns você foi aprovado!')
elif (media >= 6.0 and media <= 7.4):
    print('Coneito C, você foi aprovado!')
elif (media >= 4.0 and media <= 5.9):
    print('Coneito D, parabéns você foi reprovado!')
elif media <= 4.0:
    print('Coneito E, parabéns você foi reprovado!')
