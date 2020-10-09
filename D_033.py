n1 = int(input('Digite o primeiro nr.: '))
n2 = int(input('Digite o segundo nr.: '))
n3 = int(input('Digite o terceiro nr.: '))
menor = maior = n1
# Encontrando o MENOR
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Encontrando o MAIOR
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O MAIOR valor digitado foi {maior}')
print(f'O MENOR valor digitado foi {menor}')


