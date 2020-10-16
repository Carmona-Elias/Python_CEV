Aluno = dict()
Aluno['Nome'] = str(input('Digite seu nome: ')).strip()
Aluno['Media'] = float(input(f'Digite a media de {Aluno["Nome"]}: '))
if 'Media' in Aluno:
    if Aluno['Media'] < 10:
        Aluno['Situacao'] = 'Reprovado'
    elif 10 <= Aluno['Media'] < 14:
        Aluno['Situacao'] = 'Admidito ao Exame'
    elif Aluno['Media'] >= 14:
        Aluno['Situacao'] = 'Dispensado'
for key in Aluno.keys():
    print(f'{key}      ', end=' ')
print()
for value in Aluno.values():
    print(f'{value}    ', end=' ')
