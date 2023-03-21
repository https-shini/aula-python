#Exemlo 02

import os
os.system('cls' or 'clear')

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

if A > B and B < C:
    print("O menor valor é o B")
    print("Valores digitados: ", A, "-", B, "-", C)

