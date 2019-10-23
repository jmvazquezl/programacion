# JOSE MANUEL - P5E11 -  PROGRAMA QUE PIDA UN NÚMERO E IMPRIMA SUS DIVISORES

num = int(input('Dame un número: '))

print('Los divisores de', num, 'son', end=': ')

for i in range(num):
    i = i + 1
    if (num % i == 0):
        print(i, '', end='')
