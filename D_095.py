jogador = dict()
base_Jogador = []
golos = []
totGolos = 0
while True:
    golos.clear()
    jogador['Nome'] = str(input('Nome do Jogador: '))
    TotJogos = int(input(f'No. de Jogos realizados por {jogador["Nome"]}: '))
    for partida in range(TotJogos):
        score = int(input(f'  Quantos golos na {partida + 1}a. partida: '))
        totGolos += score
        golos.append(score)
    jogador['Qtd. golos'] = golos[:]
    jogador['Total'] = totGolos
    base_Jogador.append(jogador.copy())
    usuario = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    while usuario not in 'NS':
        print('Opcao Invalida. Tente Novamente.')
        usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if usuario in 'N':
        break
print(jogador)
print('-=-'*20)
print(f'{"Cod":<5}', end=' ')
for k in jogador.keys():
    print(f'{k:<15}', end=' ')
print()
print('-'*50)
for pos, jogador in enumerate(base_Jogador):
    print(f'{pos:<5}', end=' ')
    for d in jogador.values():
        print(f'{str(d):<18}', end='')
    print()
print('-'*50)
while True:
    view = int(input('Mostrar dados de que jogador? [999 para parar] '))
    if view == 999:
        break
    if view >= len(base_Jogador):
        print(f'Erro!! Nao existe jogador com codigo {view}')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {base_Jogador[view]["Nome"]}')
        for key, value in enumerate(base_Jogador):
            if key == view:
                for pos, val in enumerate(value["Qtd. golos"]):
                    print(f'  No jogo {pos + 1} fez {val} golos')
    print('-'*50)
print('<<< Programa Encerrado >>>')
