# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("1° n°: "))
n2 = int(input("2° n°: "))
n3 = int(input("3° n³: "))
lista = [n1, n2, n3]
lista.sort()
print(f"Abalisando os némeros {lista}, pode-se concluir que:")
print(f"O maior é {lista[2]} e o menor é {lista[0]}")

# No video foi feito assim
'''
n1 = int(input("1° n°: "))
n2 = int(input("2° n°: "))
n3 = int(input("3° n³: "))
# verificando menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")
'''