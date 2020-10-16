jogador = dict()
golos = []
totGolos = 0
jogador['Nome'] = str(input('Nome do Jogador: '))
TotJogos = int(input(f'No. de Jogos realizados por {jogador["Nome"]}: '))
for partida in range(TotJogos):
    score = int(input(f'  Quantos golos na {partida + 1}a. partida: '))
    totGolos += score
    golos.append(score)
jogador['Qtd. golos'] = golos[:]
jogador['Total'] = totGolos
print('-=-'*20)
print(jogador)
print('-=-'*20)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')
print('-=-'*20)
print(f'O jogador {jogador["Nome"]} realizou {TotJogos} partidas.')
for pos, goal in enumerate(jogador['Qtd. golos']):
    print(f'  => Na partida {pos + 1} marcou {goal} golo(s). ')
print(f'Foi um total de {totGolos} golo(s).')
