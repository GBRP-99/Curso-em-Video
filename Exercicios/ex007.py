# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = input("O nome do aluno é: ")
n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))
print(f"{nome} tirou as notas {n1:.1f} e {n2:.1f}, a média foi de {(n1+n2)/2:.1f}")
# o if é opicional
if ((n1+n2)/2) >= 6:
    print("Está arpovado")
else:
    print("Está em recuperação")
