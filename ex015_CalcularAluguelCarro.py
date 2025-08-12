pdias = 60
pkm = 0.15
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
preço = (pdias * dias) + (km * pkm)
print('O total a pagar é de R${:.2f}'.format(preço))