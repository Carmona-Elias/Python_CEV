numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('O valor digitado ja existe na lista... Nao adicionado')
    usuario = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while usuario not in 'SN':
        print('opcao Invalida. Tente Novamente.')
        usuario = str(input('Quer continuar [S/ N]: ')).strip().upper()[0]
    if usuario in 'N':
        break
numeros.sort()
print('-=-'*15)
print(f'Voce digitou os seguintes numeros: ', end='')
for nr in numeros:
    print(nr, end=' ')
print('-=-'*15)
print('Programa Terminado')
