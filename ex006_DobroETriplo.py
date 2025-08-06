black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
azm = '\033[36m'
cinza = '\033[37m'

n1 = int(input('\033[7mDigite um número{}'.format('\033[m')))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)
print('{}Você digitou {}{}\nO dobro desse número é {}'.format(blue, n1, purple, n2))
print('{}O triplo é {} e a raiz quadrada é {:.2f}'.format(azm, n3, n4))
