# JOSE MANUEL - P5E4 -  ESCRIBE UN PROGRAMA QUE PIDA UN NÚMERO Y CALCULE SU FACTORIAL

num1 = int(input('Escribe el primer numero: '))

factorial = 1
for i in range(num1):
    factorial = (i + 1) * factorial
print('El factorial de', num1, 'es:', factorial, '')
