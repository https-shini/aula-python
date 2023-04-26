#Aula 06 - Exercício 05

import os, math
os.system('cls' or 'clear')

area = int(input('Digite a área a ser pintada em m²:'))
litro = area//3
lata = math.ceil(litro/18)
valor= lata * 80

print(f'Você precisa comprar {lata} lata(s)')
print(f'O valor total a pagar será R$ {valor}')
