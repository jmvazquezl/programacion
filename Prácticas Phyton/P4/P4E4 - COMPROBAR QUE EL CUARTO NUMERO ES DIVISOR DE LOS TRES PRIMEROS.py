# JOSE MANUEL - P4E4 - PIDA NUMEROS Y COMPROBAR SI EL CUARTO ES DIVISOR DE LOS
# TRES PRIMEROS.

num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))
num3 = int(input('Introduce el tercer numero: '))
num4 = int(input('Introduce el cuarto numero: '))

if (num1 % num4 == 0) and (num2 % num4 == 0) and (num3 % num4 == 0):
    print('', num4, 'Es divisor de los numeros:', num1, num2, num3, '')

else:
    print('', num4, 'No es divisor de todos los numeros')
