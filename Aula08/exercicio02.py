#Aula 08 - Exercício 02

import os, math
os.system('cls' or 'clear')

print('Entrada:')
arquivo = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = int(input('Digite a velocidade do link de internet em Mbps: '))
sec = arquivo/(velocidade/8)
segundo = sec%60
min = sec%3600//60

print('Saida:')
print(f'Tempo aproximado para download é de: {min} minuto(s) e {segundo} segundos(s)!')
