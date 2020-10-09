soma = cont = 0
for c in range(6):
    n = int(input(f'Digite o {c+1}o numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma do todos os {cont} numeros pares digitados vale {soma}')
