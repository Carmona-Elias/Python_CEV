velocidadeCarro = float(input('Qual e velovidade do carro? '))
if velocidadeCarro > 80:
    print(f'Voce estava circulando a {velocidadeCarro}Km/h')
    print(f'Voce sera multado no valor de R$ {(velocidadeCarro - 80) * 7}')
else:
    print('Boa viagem! Conduza com prudencia')
