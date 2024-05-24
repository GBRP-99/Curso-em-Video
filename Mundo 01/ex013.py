sal = float(input("O salário do funcionário é de R$"))
aum = float(input("QUal a porcentagem (%) do aumento?"))
print(f"Com aumento de 15% ele passa a receber {sal+(sal*aum/100):.2f}")
