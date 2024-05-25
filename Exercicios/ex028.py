# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
x = random.randint(0, 5)
print("Gerando um número...")
time.sleep(1)
u = int(input("Digite um numero: "))
print("Comparando...")
time.sleep(1)
if u == x:
    print("Você acertou!")
    print(f"N? gerado foi {x} e seu chute foi {u}")
else:
    print("Você errou!")
    print(f"N? gerado foi {x} e seu chute foi {u}")
