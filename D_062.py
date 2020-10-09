a1 = int(input('Digite o primeiro termo: '))
d = int(input('Digite a razao: '))
n = int(input('Quantos termos pretende mostrar a soma? '))
cont = 1
soma = 0
while n != 0:
    print('A soma entre ',end='')
    while cont != n +1:
        soma += (a1 + (cont - 1) * d)
        print(a1 + (cont - 1) * d)
        cont += 1
    print(f'vale {soma}')
    print('Pretende mostrar a soma de mais termos? [0 para sair] ')
    n = int(input('Quantos termos: '))
print('Terminado')