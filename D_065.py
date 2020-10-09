from time import sleep
usuario = 'S'
soma = cont = maior = menor = 0
while usuario not in 'N':
    n = int(input('Digite um numero: '))
    usuario = str(input('Pretende continuar? [S/N]: ')).strip().upper()[0]
    while usuario not in 'NS':
        print('Dados invalidos. Tente Novamente.')
        usuario = str(input('Pretende continuar? [s/N]')).strip().upper()[0]
    soma += n
    cont += 1
    if usuario != 'N':
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
print('Analisando os dados >>>')
sleep(1)
print(f'Ao todo foram digitados {cont} nrs.')
print(f'A media vale {soma / cont}')
print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')
