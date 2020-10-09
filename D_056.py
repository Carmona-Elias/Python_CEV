TotIdade = MaiorIdadeF = MaiorIdadeM = 0
nomevelho = ''
for c in range(4):
    print(f'----- {c+1} Pessoa -----')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    TotIdade += idade
    if c == 0 and sexo == 'M':
        MaiorIdadeM = idade
        nomevelho = nome
    if sexo in 'M':
        if idade > MaiorIdadeM:
            MaiorIdadeM = idade
            nomevelho = nome
    elif sexo in 'F' and idade < 20:
        MaiorIdadeF += 1
print(f'A media de idade do grupo e de {TotIdade/4:.2f}.')
print(f'O nome do homem mais velho e {nomevelho} e tem {MaiorIdadeM} anos.')
print(f'Ao todo tem-se {MaiorIdadeF} mulher(es) menor(es) de 20 anos.')

