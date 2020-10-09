n = int(input('Digite um numero entre [0 - 10000]: '))
print(f'Unidades: {n//1 % 10}')
print(f'Dezenas: {n//10 % 10}')
print(f'Centenas: {n//100 % 10}')
print(f'Milhares: {n//1000 %10}')

