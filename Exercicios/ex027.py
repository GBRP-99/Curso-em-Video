# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo: ")).strip().upper()
print(f"Seu primeiro nome é {nome.split()[0]}.")
print(f"E seu ultimo nome é {nome.split()[-1]}.")
