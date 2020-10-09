usuario = str(input('Digite uma expressao matematica: '))
pa = pf = 0
for letra in usuario:
    if letra == '(':
        pa += 1
    elif letra == ')':
        pf += 1
if pa == pf:
    print('A sua expressao esta correcta.')
else:
    print('A sua expressao esta incorrecta.')
