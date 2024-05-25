# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import datetime
ano = int(input("Digite o ano para saber se ele é bissexto ou não(digite 0 para ver o ano atual): "))
if ano == 0:
    ano = datetime.date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano de {ano} é Bissexto")
else:
    print(f"O ano de {ano} não é Bissexto")
