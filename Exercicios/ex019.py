# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = str(input("O 1° aluno é:"))
a2 = str(input("O 2° aluno é:"))
a3 = str(input("O 3° aluno é:"))
a4 = str(input("O 4° aluno é:"))
# o sorteio é uma lista que entre [] contem os objetos coletados
sorteio = [a3, a4, a2, a1]
print(f"Quem deve apagar o quadro é {choice(sorteio)}")
