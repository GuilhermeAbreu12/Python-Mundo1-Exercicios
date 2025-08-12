'''Ex.023'''
num = int(input('Digite um número entre 1 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
   
print('Sua unidade é {}'.format(u))
print('Sua dezena é {}'.format(d))
print('Sua centena é {}'.format(c))
print('Sua unidade de milhar é {}'.format(m))
