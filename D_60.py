n = int(input('Digite um numero: '))
i = n
fact = 1
print(f'{n}! = ', end='')
while i > 0:
    print(f'{i} ', end='')
    if i > 1:
        print('x ', end='')
    else:
        print('= ', end='')
    fact *= i
    i -= 1

print(f'{fact}')

# for c in range(n, 0, -1):
#     fact *= (n * c)
#     n -= 1
# print(fact)

