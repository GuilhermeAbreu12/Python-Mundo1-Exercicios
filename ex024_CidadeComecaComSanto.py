cidade = input('Digite o nome de uma cidade: ').strip().lower()
divisão = cidade.split()

print('Essa cidade começa com "Santo"?: {}'.format("santo" in divisão[0]))