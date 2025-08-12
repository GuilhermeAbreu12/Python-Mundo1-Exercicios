'''Ex.022'''
nome = str(input('Digite seu nome completo: ')).strip()
caracteres = nome.split()
carac2 = len(caracteres)
l1n = caracteres[0]
print('Seu nome em MAIÚSCULAS é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome inteiro tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.fin(' ')))
