from random import randint
nr = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in nr:
    print(n, end=' ')
print()
print(f'O maior valor da tupla e {max(nr)} e o menor e {min(nr)}')
