# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
print(f"Para pintar {lar*alt:.2f} metros de parede, serão necessários {(lar*alt)/2:.1f}L de tinta")
