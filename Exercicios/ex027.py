# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo: ")).strip().lower()
print(f"Seu primeiro nome é {nome.split()[0].title()}.")
print(f"E seu ultimo nome é {nome.split()[-1].title()}.")
