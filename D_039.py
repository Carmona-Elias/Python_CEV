import datetime
ano = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Qual e o seu sexo? [M/F] ')).strip().upper()[0]
idade = datetime.date.today().year - ano
if sexo in 'M':
    print(f'Voce tem {idade} anos.')
    if idade == 18:
        print('E altura de voce recensear!!')
    elif idade > 18:
        print(f'Ja passaram {idade - 18} anos do alistamento')
        print(f'Voce deveria recensear no ano de {ano+18}')
    else:
        print(f'Voce nao tem idade para recencear, faltam {18 - idade} anos.')
        print(f'Voce devera recencear no ano de {ano + 18}')
else:
    print('Voce nao precisa efectuar o recenseamento militar')


