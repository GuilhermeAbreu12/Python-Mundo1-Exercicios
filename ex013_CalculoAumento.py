salario = float(input('Qual é o salário do funcionário? R$'))
aumento = float((salario / 100) * 15)
novosalario = float(aumento + salario)
print('{}O novo salário com 15% de aumento é de R${}{:.2f}{}'.format('\033[36m', '\033[32m', novosalario, '\033[m'))
