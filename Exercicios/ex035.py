# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input("Digite o comprimento da 1° reta: "))
r2 = float(input("Digite o comprimento da 2° reta: "))
r3 = float(input("Digite o comprimento da 3° reta: "))
print(f"Com as medidas de {r1:.1f}, {r2:.1f} e {r3:.1f}.")
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print("Você formará um triângulo.")
else:
    print("Você não será capaz de formar um triângulo.")
