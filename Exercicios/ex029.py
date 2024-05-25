# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input("A que velocidade(km/h) estava o veiculo? "))
acima = velo - 80
if velo > 80:
    print(f"Veiculo estava a {acima}km/h acima do limite!")
    print(f"Receberá a multa de R${acima*7}")
print("Dirija com segurança e boa viagem!")
