# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
# trunc é semelhante a floor
x = float(input("Digite um número real:"))
print(f"A porção inteira de {x} é {trunc(x)}")
