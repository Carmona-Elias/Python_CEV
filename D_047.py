from time import sleep
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
        sleep(1)
print('Fim!')
