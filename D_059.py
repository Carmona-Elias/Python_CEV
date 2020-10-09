n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
usuario = 0
while usuario != 5:
    print('''Menu de Opcoes
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Numeros
    [ 5 ] Sair
    ''')
    usuario = int(input('Sua opcao: '))
    if usuario == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif usuario == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif usuario == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        else:
            print(f'{n2} > {n1}')
    elif usuario == 4:
        print('Digite os numeros novemente')
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Dgite o segundo numero: '))
    elif usuario == 5:
        print('Finalizando>>>')
    else:
        print('Opca Invalida. Tente Novamente.')
print('Programa Terminado')

