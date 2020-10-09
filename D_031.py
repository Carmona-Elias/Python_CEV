dist = float(input('Introduza a distancia da viagem [Km]: '))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f'A sua passagem vale R$ {preco:.2f}')
