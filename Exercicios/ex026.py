# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

msg = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra 'A' se repete {msg.count('A')}x")
print(f"Sua primeira aparição é {msg.find('A')}")
print(f"E a sua ultima aparição é {msg.rfind('A')}")
