num = input('Digite um número: ')
num = float(num)

for mult in range(9, -2, -1):
    print('{} x {} = {}'.format(num, mult, mult * num))
