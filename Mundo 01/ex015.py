# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input("Quantos dias o carro foi locado? "))
km = int(input("Quantos km ele rodou? "))
print(f"A diaria do carro custou R${dia*60} e os Km's R${km*0.15}\nO total devido é de R${(dia*60)+(km*0.15):.2f}")
