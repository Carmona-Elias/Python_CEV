lista = ('Lapis', 1.75, 'Borracha', 2, 'Pao', 10, 'Leite', 50.5, 'Bolacha', 12)
print('-'*40)
print(f'{"Listagem de precos":^30} ')
print('-'*40)
for pos, pr in enumerate(lista):
    if pos % 2 == 0:
        print(f'{pr:.<30}', end='')
    else:
        print(f'R${pr:>7.2f}')
print('-'*40)
