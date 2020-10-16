def area(c, l):
    print(f'A area de um terreno de {c}x{l} e de {c * l}m^2')


print('Controle de Terrenos')
print('-'*20)
largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))
area(comprimento, largura)
