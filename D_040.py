nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Com media {media:.2f} ', end='')
if media >= 7.0:
    print('voce esta \033[1;32mAprovado\033[m')
elif 5.0 <= media <= 6.9:
    print(f'voce esta em \033[1;33mRecuperacao\033[m')
else:
    print(f'voce esta \033[1;31mReprovado\033[m')
