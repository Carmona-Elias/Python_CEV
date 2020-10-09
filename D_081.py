num = list()
cont = 0
while True:
    num.append(int(input('Digite um numero: ')))
    cont += 1
    usuario = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    while usuario not in 'SN':
        print('Opcao Invalida. Tente Novamente.')
        usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if usuario in 'N':
        break
print(f'Ao todo foram digitados {cont} numeros.')
print(f'Em ordem de digitacao temos: ', end='')
for n in num:
    print(n, end=' ')
print()
numc = num[:]
num.sort(reverse=True)
print(f'Em ordem decrescente temos: ', end='')
for n in num:
    print(n, end=' ')
print()
if 5 in numc:
    print('O numero 5 esta na lista e foi digitado na(s) posicao(oes) ', end='')
    for pos, value in enumerate(numc):
        if 5 == value:
            print(pos + 1, end=' ')
else:
    print('O numero 5 nao consta da lista.')
