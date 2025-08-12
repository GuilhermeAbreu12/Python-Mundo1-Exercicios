reais = float(input('Quantos reais você tem?'))
dólar = reais / 5.65
euro = reais / 6.39
print('Com R${} você pode comprar {:.4} dólares e {:.4} euros'.format(reais, dólar, euro))
