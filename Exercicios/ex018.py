# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang = float(input("Digite o angulo:"))
print(f"O sedno de {ang} é {sin(radians(ang)):.2f}")
print(f"o coseno de {ang} é {cos(radians(ang)):.2f}")
print(f"A tangente de {ang} é {tan(radians(ang)):.2f}")
