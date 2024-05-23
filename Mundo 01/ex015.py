dia = int(input("Quantos dias o carro foi locado? "))
km = int(input("Quantos km ele rodou? "))
print(f"A diaria do carro custou R${dia*60} e os Km's R${km*0.15}\nO total devido é de R${(dia*60)+(km*0.15):.2f}")
