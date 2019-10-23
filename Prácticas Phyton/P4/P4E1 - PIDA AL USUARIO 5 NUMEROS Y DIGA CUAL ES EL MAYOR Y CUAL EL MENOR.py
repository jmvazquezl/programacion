# JOSE MANUEL - P4E1 - PIDA AL USUARIO 5 NÚMEROS Y DIGA CUAL ES EL MAYOR Y CUÁL EL MENOR

num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))
num3 = int(input('Introduce el tercer numero: '))
num4 = int(input('Introduce el cuarto numero: '))
num5 = int(input('Introduce el quinto numero: '))

mayor = num1
menor = num1

if (mayor < num1):
    mayor = num1
if (mayor < num2):
    mayor = num2
if (mayor < num3):
    mayor = num3
if (mayor < num4):
    mayor = num4
if (mayor < num5):
    mayor = num5

if (menor > num1):
    menor = num1
if (menor > num2):
    menor = num2
if (menor > num3):
    menor = num3
if (menor > num4):
    menor = num4
if (menor > num5):
    menor = num5

print('El numero mas grande es', mayor, 'y el numero menor es', menor, '')
