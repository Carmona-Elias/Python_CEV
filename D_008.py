from time import sleep
print('Conversor de Unidades')
medida = float(input('Introduza uma medida em metros: '))
print('Processando pedido>>>')
sleep(2)
print(f'{medida} m >> {medida*100} cm >> {medida*1000} mm')
print('Concluido')
