matriz = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
for coluna in range(3):
    for linha in range(3):
        n = int(input(f'Digite um numero na posicao [{coluna + 1}, {linha + 1}]: '))
        matriz[int(coluna)][int(linha)] = n
print('-=-'*20)
for coluna in matriz:
    for c in range(3):
        print(f'[ {coluna[c]:^5} ]', end=' ')
    print()
