n = input('Digite algo: ')
print(f'O tipo primitivo do valor introduzido e: {type(n)}')
print(f'E alfa-numerico? {n.isalnum()}')
print(f'E numerico? {n.isnumeric()}')
print(f'E ascii? {n.isascii()}')
print(f'E decimal? {n.isdecimal()}')
print(f'E um identificador? {n.isidentifier()}')
print(f'Esta capitalizada? {n.istitle()}')
print(f'E printable? {n.isprintable()}')
