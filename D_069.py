maior18 = totH = M20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = input('Digite sua idade: ')
    while not idade.isnumeric():
        print('Dados Invalidos. Tente Novamente.')
        idade = input('Digite sua idade.')
    if int(idade) > 18:
        maior18 += 1
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Dados invalidos. Tente Novamente.')
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo in 'M':
        totH += 1
    if sexo in 'F' and int(idade) < 20:
        M20 += 1
    print('-'*30)
    usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while usuario not in 'SN':
        print('Dados Invalidos. Tente novamente.')
        usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if usuario in 'N':
        break
print(f'Ao todo foram registradas {maior18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {totH} homens.')
print(f'Foram cadastradas {M20} mulheres menores de 20 anos.')
