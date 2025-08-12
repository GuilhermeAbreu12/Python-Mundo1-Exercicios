# Aula 10: Condições (Parte 1)
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Quantos Km/h seu carro está?: Km/h '))
limite = 80
if vel == 80:
    print('\033[33m Tome cuidado você está no limite de velocidade!!')
if vel < 80:
    print('\033[32m Parabéns você está abaixo do limite de velocidade!')
if vel > 80:
    print('\033[31m Infelizmente você foi multado no valor de R${:.2f}'.format((vel - 80) * 7.00))