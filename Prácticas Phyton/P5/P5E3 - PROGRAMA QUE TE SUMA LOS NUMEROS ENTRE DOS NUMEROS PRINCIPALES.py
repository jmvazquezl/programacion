# JOSE MANUEL - P5E3 - UN PROGRAMA QUE PIDA DOS NUMEROS Y ESCRIBA LA SUMA DE ENTEROS DESDE
# EL PRIMERO HASTA EL ULTIMO

num1 = int(input('Escribe el primer numero: '))
num2 = int(input('Escribe el segundo numero: '))

suma = 0

for i in range(num1, num2):
    suma = i + suma
    print('', i, '+', end='')

print('', num2, '=', suma, '')
