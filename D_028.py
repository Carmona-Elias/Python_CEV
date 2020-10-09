import random
from time import sleep
computador = random.randint(0, 5)
print('-=-'*20)
print('Vou pensar num numero entre 0 e 5! Tente adivinhar.')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei ? '))
print('Processando...')
sleep(2)
if computador == jogador:
    print('PARABENS! Voce me Venceu.')
else:
    print('Voce perdeu. Tente Novamente')
print(f'Voce pensou no nr. {jogador} e EU pensei no nr. {computador}')
