galera = list()
dado = []
Mpeso = []
mPeso = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while usuario not in 'NS':
        print('Opcao Invalida. Tente Novamente.')
        usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if usuario in 'N':
        break
for pessoa in galera:
    if pessoa[1] == maior:
        Mpeso.append(pessoa[0])
    elif pessoa[1] == menor:
        mPeso.append(pessoa[0])
print('-=-'*20)
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'O maior peso foi de {maior} kg cuja listagem e: {Mpeso}: ')
print(f'O menor peso foi de {menor} Kg cuja listagem e: {mPeso}')
