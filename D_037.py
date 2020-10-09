import math
print('-=-'*20)
print('Conversor de Bases Numericas')
print('-=-'*20)
numero = int(input('Digite um numero: '))
usuario = int(input('Esolha uma das bases para conversao: \n'
                    '[ 1 ] para Binario\n'
                    '[ 2 ] para Octal\n'
                    '[ 3 ] para Hexadecimal\n'
                    'Sua Opcao: '))
if usuario == 1:
    print(bin(numero)[2:])
elif usuario == 2:
    print(oct(numero)[2:])
elif usuario == 3:
    print(hex(numero)[2:])
else:
    print('\033[1;31m Opcao invalida. Tente Novamente.\033[m')


