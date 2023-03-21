import os
os.system('cls' or 'clear')

num = float(input('Digite um numero de 0 a 9: '))

resposta = "Parabens" if num<=9 else 'Errado'
print(f'O numero digitado é {num}, {resposta}')
