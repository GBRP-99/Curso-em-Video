# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite o nome da cidade: ")).strip().upper()
print(f"A cidade começa com o nome 'Santo'? {cidade[:5] == 'SANTO'}")
