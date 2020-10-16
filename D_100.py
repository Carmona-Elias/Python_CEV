from random import randint
from time import sleep
numeros = []


def sorteia():
    for c in range(5):
        numeros.append(randint(1, 10))
    print(f'Sorteando {len(numeros)} valores da lista:  ', end=' ')
    for n in numeros:
        print(n, end=' ')
        sleep(1)
    print('Pronto!')


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos pares de {lst} vale {soma}')


sorteia()
somaPar(numeros)
