# Aula 10: Condições (Parte 1)
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
print('Estou pensando em um número de 1 a 10.')
start = int(input('Tente adivinhar o número que eu estou pensando: '))
num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if start == num:
    print('Você acertou! Eu pensei no número {}'.format(num))
else:
    print('Errou! Eu pensei no número {}, eu ganhei!'.format(num))