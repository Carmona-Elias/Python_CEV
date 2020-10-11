listaGeral = [[], []]
for c in range(7):
    n = int(input(f'Digite um numero na posicao {c + 1}: '))
    if n % 2 == 0:
        listaGeral[0].append(n)
    else:
        listaGeral[1].append(n)
listaGeral[0].sort()
listaGeral[1].sort()
print('-=-'*20)
print('Os valores pares digitados foram: ', end=' ')
for v in listaGeral[0]:
    print(v, end=' ')
print()
print('Os valores impares digitados foram: ', end=' ')
for v in listaGeral[1]:
    print(v, end=' ')
print()
