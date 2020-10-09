print('Gerador de PA')
print('-='*20)
a1 = int(input('Digite o primeiro termo: '))
d = int(input('Digite a razao: '))
soma = 0
cont = 1
print('A soma entre ', end=' ')
while cont != 11:
    soma += (a1 + (cont - 1) * d)
    print(a1 + (cont - 1)*d, end=' ')
    cont += 1
print(f'e igual a {soma}')
