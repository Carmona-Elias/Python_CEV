n = int(input('Digite o numero de termos: '))
a1 = cont = 0
a2 = 1
print(f'{a1}->{a2}', end='->')
while cont != n-2:
    an = a1 + a2
    if n != n - 4:
        print(an, end='->')
    else:
        print(an, end='')
    aux = a2
    a1 = a2
    a2 = an
    cont += 1
print('Fim')
