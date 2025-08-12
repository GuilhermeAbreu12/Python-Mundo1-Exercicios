# Aula 10: Condições (Parte 1)
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = input('Digite um número: ')
b = input('Digite outro número: ')
c = input('Digite mais um número: ')

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))