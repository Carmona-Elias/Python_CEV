from random import randint
computador = randint(0, 10)
tentatvas = 0
acertou = False
print('O computador pensou num numero entre 0 e 10. ')
while not acertou:
    jogador = int(input('Tente adivinhar: '))
    tentatvas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f'O coputador pensou no nr. {computador} e vc {jogador}.')
            print(f'Dica: Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print(f'O computador pensou no nr. {computador} e vc {jogador}.')
            print(f'Dica: Menos... Tente mais uma vez.')

print(f'Parabens! Voce Venceu.\n Voce precisou de {tentatvas} tentativas.')
