numeros = list()
maior = menor = 0
for cont in range(0, 5):
    numeros.append(int(input(f'Digite um numero na posicao {cont + 1}: ')))
for key, value in enumerate(numeros):
    if key == 0:
        maior = menor = value
    elif value >= maior:
        maior = value
    elif value <= menor:
        menor = value


print('-=-'*30)
print('Voce digitou os numeros ', end=' ')
for n in numeros:
    print(n, end=' ')

print(f'O maior numero digitado foi {maior} na(s) posicao(oes) ', end='')
for p, n in enumerate(numeros):
    if maior == n:
        print(p + 1, end='...')
print()
print(f'O menor numero digitado foi {menor} na(s) posicao(oes) ', end='')
for pos, nr in enumerate(numeros):
    if menor == nr:
        print(pos + 1, end='...')
