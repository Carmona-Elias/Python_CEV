lista = ('Amendoim', 'Melancia', 'Ananas', 'Banana', 'Maca', 'Abacate', 'Melao', 'Kiwi')
for palavra in lista:
    print(f'Na palavra temos {palavra.upper():<10}', end=' ')
    for p in palavra:
        if p in 'AaEeIiOoUu':
            print(f'{p.lower()}', end=' ')
    print()
