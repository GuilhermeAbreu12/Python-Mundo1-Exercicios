# Aula 9: Manipulando texto
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A";
# - Em que posição ela aparece a primeira vez;
# - Em que posição ela aparece a última vez.

frase = str(input('Digite algo: ')).lower().strip()
vezes = frase.count('a')

print('A letra A aparece {} vezes nesse texto'.format(vezes))
print('A primeira vez que ela apareceu foi na posição {}'.format(frase.find('a') + 1))
print('A última vez que ela apareceu foi na posição {}'.format(frase.rfind('a') + 1))
