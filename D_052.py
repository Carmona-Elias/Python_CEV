n = int(input('Digite um numero: '))
contdiv = 0
for c in range(1, n+1):
    if n % c == 0:
        contdiv += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO numero {n} e divisivel {contdiv} vezes por isso ', end=' ')
if contdiv == 2:
    print(f'e PRIMO')
else:
    print('nao e PRIMO')
