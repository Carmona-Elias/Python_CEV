from random import randint
computador = randint(0, 5)
cont = 0
print('-=-'*10)
print('Vanos Jogar PAR OU IMPAR ')
print('-=-'*10)
while True:
    jogador = int(input('Digite um numero: '))
    Total = jogador + computador
    palpite = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    if Total % 2 == 0:
        res = 'PAR'
    else:
        res = 'IMPAR'
    if Total % 2 == 0 and palpite in 'P':
        cont += 1
        print(f'Voce jogou {jogador} e o computador {computador}. Total {Total} DEU {res}')
        print('-'*20)
        print('Voce VENCEU! ')
        print('Vamos jogar novamente....')
        print('-=-'*10)
    elif Total % 2 != 0 and palpite in 'I':
        cont += 1
        print(f'Voce jogou {jogador} e o computador {computador}. Total {Total} DEU {res}')
        print('-'*20)
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        print('-=-'*10)
    else:
        print(f'Voce jogou {jogador} e o computador {computador}. Total {Total} DEU {res}')
        break
print('-=-'*10)
print('Voce PERDEU!!')
print(f'GAME OVER!! Voce venceu {cont} vez(es).')

