#Exemlo 05

import os
os.system('cls' or 'clear')


compra = float(input('Digite o valor total da compra: '))
print('Vaores de parcelas disponíveis: [2] [4] [6] [8]')

parcelas = int(input('Digite uma das opções: '))

if parcelas == 2:
    valor = compra * 1.03
elif parcelas == 4:
    valor = compra * 1.07
elif parcelas == 6:
    valor = compra * 1.09
elif parcelas == 8:
    valor = compra * 1.12
else:
    valor = 0

if valor > 0:
    print(f'Valor de cada parcela seria: R$ {valor/parcelas}')
else:
    print('Tipo de parcelameto indisponivel!')
