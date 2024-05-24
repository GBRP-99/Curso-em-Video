from random import shuffle
a1 = str(input("O 1° aluno é:"))
a2 = str(input("O 2° aluno é:"))
a3 = str(input("O 3° aluno é:"))
a4 = str(input("O 4° aluno é:"))
lista = [a4, a2, a1, a3]
# shuffle serve para embaralhar, mas não pode ser adicionado no print
# caso adicionado ele não gera a lista, apenas mistura e exibe "NONE"
shuffle(lista)
print("A ordem de apresentação é:")
for indice, aluno in enumerate(lista, start=1):
    print(f"{indice}. {aluno}")
    # "indice" está ligado ao "start=1" e começa a contagem em 1
    # "aluno é onde será armazenado o objeto que estiver na lista que já foi embaralhada"
    # "enumerate" vai fazer a lista com um quebra após cada item da lista
    # "indice" vai mostrar um numero, enquanto "aluno" mostra o objeto da lista (a1, a2, a3, a4)

# print(f"A ordem de apresentação é {lista}")
# outra forma sem o "for", pnde exibe um resultado mais simples
