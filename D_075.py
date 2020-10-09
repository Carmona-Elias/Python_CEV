n1 = int(input('Digite o 1o numero: '))
n2 = int(input('Digite o 2o numero: '))
n3 = int(input('Digite o 3o numero: '))
n4 = int(input('Digite o 4o numero: '))
base = (n1, n2, n3, n4)
print(f'Os valores digitados foram: {base}')
print(f'O numero 9 apareceu {base.count(9)} vez(es)')
if 3 in base:
    print(f'O primeiro numero 3 foi digitado na posicao {base.index(3) + 1}')
else:
    print('O numero 3 nao foi encontrado.')
print('Os numeros pares digitados foram: ', end=' ')
for nr in base:
    if nr % 2 == 0:
        print(nr, end=' ')
