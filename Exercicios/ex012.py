# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Qual o preço do produto R$"))
print(f"Com desconto de 5% ele sai por R$ {preco-(preco*5/100)}")
