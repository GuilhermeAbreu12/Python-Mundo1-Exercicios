# Aula 10: Condições (Parte 1)
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('-=' * 20)
print('{}Analizador de Triângulos{}'.format('\033[34m', '\033[m'))
print('-=' * 20)

n = input('Digite o comprimento da primeira reta')
n2 = input('Digite o comprimento da segunda reta')
n3 = input('Digite o comprimento da terceira reta')

if n < n2 + n3 and n2 < n + n3 and n3 < n + n2:
    print('É possivel sim formar um triângulo')
else:
    print('Não é possivel formar um triângulo')