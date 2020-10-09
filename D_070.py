total = maisMil = maisBarato = cont = 0
barato = ''
listaNome = []
ListaBarato = []
print('-'*30)
print('LOJA SUPER BARATAO')
print('-'*30)
while True:
    nome = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preco: R$'))
    usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while usuario not in 'SN':
        print('Dados Invalidos. Tente Novamente.')
        usuario = str(input('Quer continuar? [S/N]: '))
    total += preco
    cont += 1
    if preco > 1000:
        maisMil += 1
    if cont == 1:
        maisBarato = preco
        barato = nome
    else:
        if preco < maisBarato:
            maisBarato = preco
            barato = nome
    if usuario in 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total gasto vale R${total:.2f}')
print(f'Ao todo sao {maisMil:.2f} produtos que custam mais de R$1000')
print(f'O produto mais barato e {barato} e custa R${maisBarato:.2f}')

