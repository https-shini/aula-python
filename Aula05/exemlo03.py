#Exemlo 03

import os
os.system('cls' or 'clear')

n1 = int(input('Digite o valor do primeiro número: '))
n2 = int(input('Digite o valor do segundo número: '))
n3 = int(input('Digite o valor do terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número')
else:
    print(f'{n3} é o maior número')
