while True:
    n = int(input('Digite um numero para ver sua tabuada: '))
    if n < 0:
        break
    i = 1
    while i <= 10:
        print(f'{n} x {i} = {n*i}')
        i += 1
    print('-'*40)
print('-'*40)
print('Programa Tabuada terminado. Volte sempre!')
