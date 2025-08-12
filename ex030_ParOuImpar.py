# Aula 10: Condições (Parte 1)
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número inteiro: '))
par = num % 2
if par == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
