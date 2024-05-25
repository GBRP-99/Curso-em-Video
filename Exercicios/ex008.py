# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

cm = float(input("Digiet os centimetros a serem calculados: "))
print(f"Corresponde a {cm / 100000:.5f} Km")
print(f"Corresponde a {cm / 10000:.4f} Hm")
print(f"Corresponde a {cm / 1000:.3f} Dam")
print(f"Corresponde a {cm / 100:.2f} M")
print(f"Corresponde a {cm / 10:.1f} Dm")
print(f"Corresponde a {cm * 10:.1f} mm")
