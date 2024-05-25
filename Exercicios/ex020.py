# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input("O 1° aluno é:"))
a2 = str(input("O 2° aluno é:"))
a3 = str(input("O 3° aluno é:"))
a4 = str(input("O 4° aluno é:"))
lista = [a4, a2, a1, a3]
# shuffle serve para embaralhar, mas não pode ser adicionado no print
# caso adicionado ele não gera a lista, apenas mistura e exibe "NONE"
shuffle(lista)
print(f"A ordem de apresentação é\n {lista}")
