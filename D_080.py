numeros = list()
for cont in range(0, 5):
    n = int(input(f'Digite um numero na posicao {cont + 1}: '))
    if cont == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista. ')
    else:
        for c in range(len(numeros)):
            if n <= numeros[c]:
                numeros.insert(c, n)
                print(f'Adicionado na posicao {c} da lista.')
                break
print(numeros)
