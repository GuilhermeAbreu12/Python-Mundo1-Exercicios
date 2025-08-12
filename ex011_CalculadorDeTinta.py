largura = float(input("Quantos metros tem de largura? "))
altura = float(input("Quantos metros tem de altura? "))
area = largura * altura
tinta = float(area / 2)
print('Esse terreno tem a dimensão{} x {} e por isso precisará de {} litros de tinta para pintar ele'.format(largura, altura, tinta))