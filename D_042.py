r1 = float(input('Digite o comprimento do primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))
print(f'Com os segmentos {r1:.2f}, {r2:.2f} e {r3:.2f} ', end='')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podemos formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('Equilatero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isosceles.')
    else:
        print('Escaleno.')
else:
    print('Nao se pode formar um triangulo.')
