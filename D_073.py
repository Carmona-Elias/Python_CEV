clasificacao = ('A. Mineiro', 'Internacional', 'S. Paulo', 'Palmeiras', 'V. Gama', 'Flamengo', 'Chapecuense', 'Santos', 'Fortaleza', 'Fluminense', 'Ceara', 'Gremio', 'Corinthians', 'A. Goianiense', 'A. Paranaense', 'Coritiba', 'Bragantino', 'Botafogo', 'Bahia', 'Goias')
count = posicao = 0
print('Os cinco primeiros classificados sao: ')
for cont in range(6):
    print(clasificacao[cont])

print('Os ultimos quatro classificados sao: ')
for cont in range(len(clasificacao) - 1, -1, -1):
    print(clasificacao[cont])
    count += 1
    if count == 4:
        break

print('Em orde alfabetica a classificacao apresenta-se da seguinte forma: ')
print(sorted(clasificacao))

for pos, time in enumerate(clasificacao):
    if 'Chapecuense' in time:
        posicao = pos
print(f'O time Chapecuense encontra-se na posicao {posicao + 1}')

