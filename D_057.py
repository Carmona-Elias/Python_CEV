sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dados Invalidos. Tente Novamente. ')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso. Obrigado.')
