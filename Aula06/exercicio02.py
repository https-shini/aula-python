#Aula 06 - Exercício 02

import os
os.system('cls' or 'clear')

segundos = int(input('Digie a quantidade de segudos: '))

horas = segundos//3600
min = segundos%3600//60
seg = segundos%60

print(f'{horas} horas(s), {min} minutos(s), {seg} segundo(s).')
