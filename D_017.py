from math import pow, hypot, sqrt
cateto_1 = float(input('Digite o comprimento do primeiro cateto [C1]: '))
cateto_2 = float(input('Digite o comprimeto do segundo cateto [C2]: '))
hipotenusa = sqrt(pow(cateto_1, 2) + pow(cateto_2, 2))
print(f'A hipotenusa vale {hipotenusa}')
print(f'A hipotenusa vale {hypot(cateto_1, cateto_2)}')
