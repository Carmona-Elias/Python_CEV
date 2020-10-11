somaPar = somaTerceira = maior = 0
matriz = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
# Entrada de Dados
for linha in range(3):
    for coluna in range(3):
        n = int(input(f'Digite um numero na posicao [{linha + 1}, {coluna + 1}]: '))
        matriz[linha][coluna] = n
# Verifica: A) A soma dos valores pares
#           B) A soma dos Valores da Terceira Coluna
#           C) O maior valor da segunda coluna
for coluna in matriz:
    for ln in range(3):
        if coluna[ln] % 2 == 0:
            somaPar += coluna[ln]
    somaTerceira += coluna[2]
for valor in matriz[1]:
    if valor > maior:
        maior = valor
# Impressao da Matriz
for linha in matriz:
    for c in range(3):
        print(f'[ {linha[c]:^3} ]', end=' ')
    print()

print(f'A soma de todos valores pares vale {somaPar}')
print(f'A soma dos valores da terceira coluna vale {somaTerceira}')
print(f'O maior valor da segunda linha vale {maior}')
