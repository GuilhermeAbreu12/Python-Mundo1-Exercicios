# Aula 10: Condições (Parte 1)
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
Km = float(input('Qual é a distância da viagem em Km? '))
if Km < 200:
    preço = Km * 0.50
else:
    preço = Km * 0.45

print('A viagem vai custar R${:.2f}'.format(preço))
