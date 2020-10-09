Lista = list()
pesoM = pesom = 0
for c in range(5):
    peso = float(input('Digite seu peso [Kg]: '))
    Lista.append(peso)
    if c == 0:
        pesoM = pesom = peso
    else:
        if peso > pesoM:
            pesoM = peso
        if peso < pesom:
            pesom = peso
print(f'O maior peso foi de {max(Lista)}Kg e o menor de {min(Lista)}Kg')
print(f'-> O maior peso foi de {pesoM}Kg e o menor de {pesom}Kg')
