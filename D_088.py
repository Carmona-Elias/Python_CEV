from random import randint
from time import sleep
dado = []
jogos = []
print('-'*20)
print('JOGA NA MEGA SENA')
print('-'*20)
usuario = int(input('Quantos jogos voce quer sortear? '))
for j in range(usuario):
    for c in range(6):
        n = randint(1, 60)
        if c == 0:
            dado.append(n)
        elif n in dado:
            n = randint(1, 60)
            dado.append(n)
        else:
            dado.append(n)
    dado.sort()
    jogos.append(dado[:])
    dado.clear()
    j += 1
print('-='*3, f'Sorteando {usuario} Jogos', '-='*3)
for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}')
    sleep(1)
print('-='*5, '<Boa Sorte>', '-='*5)
