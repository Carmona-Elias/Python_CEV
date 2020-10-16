from time import sleep


def maior(*nr):
    maiorn = 0
    for n in nr:
        if n > maiorn:
            maiorn = n
    print('-=-'*15)
    print('Analisando os valores passados ...')
    sleep(0.5)
    for n in nr:
        print(n, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(nr)} valores ao todo.')
    print(f'O maior valor informado foi {maiorn}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
