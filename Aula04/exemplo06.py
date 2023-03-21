#Exemlo 6 - Aula 04

import math
num = int(input('Digite um numero inteiro positivo: '))

if num>=0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz:.2f}')

else:
    print('Não há raiz quadrada de um numero negativo em R!')
