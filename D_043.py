from math import pow
print('-=-'*10)
print('Calculadora de IMC')
print('-=-'*10)
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso/pow(altura, 2)
print(f'O IMC {IMC:.2f} indica uma pessoa ', end='')
if IMC < 17:
    print('\033[1;31mMuito Abaixo do Peso\033[m')
elif 17 <= IMC < 19:
    print('\033[1;33mAbaixo do peso\033[m')
elif 19 <= IMC < 25:
    print('\033[1;32mCom Peso Normal\033[m')
elif 25 <= IMC < 30:
    print('\033[1;33mAcima do Peso\033[m')
elif 30 <= IMC < 35:
    print('\033[1;31mCom Obesidade I\033[m')
elif 35 <= IMC < 40:
    print('\033[1;31mCom Obesidade II (severa)\033[m')
else:
    print('\033[1;31mCom Obesidade III (Morbia)\033[m')
