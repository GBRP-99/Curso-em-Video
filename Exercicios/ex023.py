# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

x = int(input("Digite um numero: "))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print(f"Analizando o numero {x}")
print(f"Milhar: {m}")
print(f"Centena {c}")
print(f"Dezena {d}")
print(f"Unidade {u}")
