import datetime
ano = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - ano
print(f'Com {idade} anos sua classificacao e ', end='')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Senior')
else:
    print('Master')
