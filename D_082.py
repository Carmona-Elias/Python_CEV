listaG = list()
listaP = list()
listaI = list()
while True:
    n = int(input('Digite um numero: '))
    listaG.append(n)
    usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while usuario not in 'NS':
        print('Dados Invalidos. Por favor tente novamente: ')
        usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if usuario in 'N':
        break
for nr in listaG:
    if nr % 2 == 0:
        listaP.append(nr)
    else:
        listaI.append(nr)
print('Voce digitou os seguintes numeros: ', end='')
for n in listaG:
    print(n, end=' ')
print()
print('Onde os numeros: ')
for n in listaP:
    print(n, end=' ')
print('sao PARES.')
for n in listaI:
    print(n, end=' ')
print('sao IMPARES')
