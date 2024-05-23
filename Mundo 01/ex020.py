from random import shuffle
a1 = str(input("O 1° aluno é:"))
a2 = str(input("O 2° aluno é:"))
a3 = str(input("O 3° aluno é:"))
a4 = str(input("O 4° aluno é:"))
lista = [a4, a2, a1, a3]
shuffle(lista)
print("A ordem de apresentação é:")
for indice, aluno in enumerate(lista, start=1):
    print(f"{indice}. {aluno}")
