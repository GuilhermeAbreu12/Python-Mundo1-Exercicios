# Aula 10: Condições (Parte 1)
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite seu salário: R$ '))
if salario > 1250.00:
    print('Seu aumento será de 10% e seu novo salário será de R${:.2f}'.format(salario * 10/100 + salario))

if salario <= 1250.00:
    print('Seu aumento será de 15% e seu novo salário será de R${:.2f}'.format(salario * 15/100 + salario))
