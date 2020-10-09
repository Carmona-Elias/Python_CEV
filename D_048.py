soma = cont = 0
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma += n
        cont += 1
print(f'A soma de todos {cont} numeros impares e multiplos de tres vale {soma}')
