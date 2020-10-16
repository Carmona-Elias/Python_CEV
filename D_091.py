from random import randint
from time import sleep
pos = 1
jogador = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogador4': randint(1, 6)
           }
print('Valores Sorteados')
for key, value in jogador.items():
    print(f'  O {key} tirou {value}')
    sleep(1)
# Ordenar o dicionario
print('Ranking dos Jogadores')
jogador_Ranking = sorted(jogador.items(), key=lambda x: x[1], reverse=True)
for value in jogador_Ranking:
    print(f'  {pos}o. lugar: {value[0]} com {value[1]}')
    pos += 1
