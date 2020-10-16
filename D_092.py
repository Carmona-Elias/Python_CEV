import datetime
Registro = dict()
Registro['Nome'] = str(input('Digite seu Nome: '))
Registro['Ano Nasc.'] = int(input('Ano de Nascimento: '))
Registro['Idade'] = datetime.date.today().year - Registro['Ano Nasc.']
Registro['CTPS'] = int(input('Carteira de Trabalho: '))
if Registro['CTPS'] != 0:
    Registro['Ano Contratacao'] = int(input('Ano Contratacao: '))
    Registro['Salario R$'] = float(input('Salario R$ '))
    Registro['Aposentadoria'] = (Registro['Ano Contratacao'] - Registro['Ano Nasc.']) + 35
print('-=-'*20)
for key, value in Registro.items():
    print(f'{key}   {value}')
