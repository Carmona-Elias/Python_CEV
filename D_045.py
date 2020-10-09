from time import sleep
import random
lista = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(lista)
print('\033[1;36m-=-\033[m'*15)
print('\033[1;35m Vamos Jogar ao Janken-pon???\033[m')
print('\033[1;36m-=-\033[m'*15)
jogador = str(input('Qual e a sua jogada?\n'
                    'Digite:\n'
                    '[Pedra]\n'
                    '[Papel]\n'
                    '[Tesoura]\n'
                    'Sua opcao: ')).strip().capitalize()
print('\033[1;35m*\033[m'*40)
print('Jan')
sleep(1)
print('ken')
sleep(1)
print('pon!!')
if computador == 'Pedra':
    if jogador == computador:
        print('\033[1;33mEmapte!!\033[m')
    elif jogador == 'Papel':
        print('\033[1;32mVoce Venceu!! Parabens.\033[m')
    elif jogador == 'Tesoura':
        print('\033[1;31m Voce perdeu!! Tente Novamente.\033[m')
    else:
        print('\033[1;31m Jogada Invalida\033[m')
elif computador == 'Papel':
    if jogador == 'Pedra':
        print('\033[1;31mVoce Perdeu!! Tente Novamente.\033[m')
    elif jogador == 'Tesoura':
        print('\033[1;32mVoce Venceu!! Parabens!\033[m')
    elif jogador == computador:
        print('\033[1;33mEmpate!!\033[m')
    else:
        print('\033[1;31m Jogada Invalida\033[m')
elif computador == 'Tesoura':
    if jogador == 'Pedra':
        print('\033[1;32mVoce Venceu!! Parabens!\033[m')
    elif jogador == 'Papel':
        print('\033[1;31m Voce Perdeu!! Tente Novamente.\033[m')
    elif jogador == computador:
        print('\033[1;33m Empate \033[m')
    else:
        print('\033[1;31m Jogada Invalida\033[m')
print(f'\033[1;34mO computador escolheu {computador} e voce {jogador}\033[m')

