dataBase = []
Mbase = []
dado = dict()
somaIdade = 0
# Entrada de Dados
while True:
    dado['nome'] = str(input('Nome: ')).strip()
    dado['idade'] = int(input('Idade: '))
    while True:
        dado['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dado['sexo'] in 'MF':
            break
        print('Erro!! Por favor digite M/ F')
    dataBase.append(dado.copy())
    # dado.clear()
    usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while usuario not in 'NS':
        print('Opcao Invalida. Tente Novamente.')
        usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if usuario in 'N':
        break
# Analise de Dados
for pessoa in dataBase:
    somaIdade += pessoa['idade']
    idadeMedia = somaIdade / len(dataBase)
    if pessoa['sexo'] in 'F':
        Mbase.append(pessoa['nome'])
# Saida de Dados
print('-=-'*20)
print(f'- Ao todo foram cadastradas {len(dataBase)} pessoas.')
print(f'- A media de idade e de {idadeMedia:.2f} anos.')
print(f'- Ao todo foram cadastradas {len(Mbase)} mulheres, nomeadamente, ', end=' ')
for pos, value in enumerate(Mbase):
    if pos != (len(Mbase) - 1):
        print(value, end=', ')
    else:
        print('e '+value + '.')
print(f'- Lista de pessoas que estao acima da media: ')
for pessoa in dataBase:
    if pessoa['idade'] > idadeMedia:
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end=' ')
        print()
print('<< ENCERRADO >>')
