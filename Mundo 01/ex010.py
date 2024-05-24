# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Quantos reais você deseja cambiar R$"))
print(f"Você pode comprar US$ {real/5.10:.2f}")
print(f"Você pode comprar  € {real/5.55:.2f}")
