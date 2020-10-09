print('Aluguel de Carros')
dias = float(input('Quantos dias alugados? '))
rodagem = float(input('Qunatos Km rodados? '))
print(f'O total a pagar pelo aluguel e de R${dias*60 + 0.15*rodagem:.2f}')
