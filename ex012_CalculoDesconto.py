preço = float(input('Digite o preço atual do produto. R$'))
desconto = float((preço / 100) * 5)
preço_desconto = float(preço - desconto)
print('O valor do produto com 5% de desconto será de R${}'.format(preço_desconto))