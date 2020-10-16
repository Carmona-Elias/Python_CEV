from time import sleep


def contador(i, f, p):
    print('-=-'*10)
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} ate {f} de {p} a {p}')
    sleep(1)
    if i > f:
        p *= -1
        f -= 1
    else:
        f += 1
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)
    print('Fim!')


contador(1, 10, 1)
contador(i=10, f=0, p=2)
print('-=-'*10)
print('Agora e sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
