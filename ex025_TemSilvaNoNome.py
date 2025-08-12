# Aula 9: Manipulando texto
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = input('Digite um nome: ').lower()
print('O nome digitado tem "Silva" no nome?: {}'.format('silva' in nome))