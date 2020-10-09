usuario = soma = cont = 0
while usuario != 999:
    usuario = int(input('Digite um numero [999 para sair]: '))
    if usuario != 999:
        soma += usuario
        cont += 1
print(f'Ao todo foram digitados {cont} numeros.')
print(f'A soma vale {soma}')
