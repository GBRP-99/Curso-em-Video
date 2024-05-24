# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input("Digite algo:")
print(f"o tipo primitivo é: {type(x)}")
print(f"É alfanumeiro? {x.isalnum()}")
print(f"É numerico apenas? {x.isnumeric()}")
print(f"É texto apenas? {x.isalpha()}")
print(f"É Computavél? {x.isascii()}")
