from time import sleep
print('-=-'*20)
print('Imprimindo os Primeiros Termos de uma P.A: ')
print('-=-'*20)
a1 = int(input('Digite o primeiro termo da P.A: '))
d = int(input('Digite a razao da P.A: '))
termo = a1 + (10 - 1)*d
for n in range(a1, termo + d, d):
    print(n, end='->')
    sleep(1)
print('Acabou')
