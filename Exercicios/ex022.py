# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao total (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo:"))
print(f"Seu nome em maiusculas é {nome.upper()}.")
print(f"Seu nome em minusculas é {nome.lower()}.")
print(f"Seu nome completo possui {len(nome.replace(" ", ""))} letras.")
print(f"Seu primeiro nome é {nome.split()[0]} e possui {len(nome.split()[0])} letras")
