# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

x = int(input("Digite um número inteiro:"))
if (x % 2) == 0:
    print(f"O número {x} é par.")
else:
    print(f"O número {x} é impar")
