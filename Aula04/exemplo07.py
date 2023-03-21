import os
os.system('cls' or 'clear')

num = float(input('Digite um numero entre 0 e 9: '))

resposta = "Parabens" if num>=0 and num<=9 else 'Errado'
print(f'O numero digitado é {num}, {resposta}')
