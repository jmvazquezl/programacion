# JOSE MANUEL - P4E2 - PIDA AL USARIO 5 NUMEROS Y DIGA SI ESTOS ESTABAN EN ORDEN
# DECRECIENTE,CRECIENTE O DESORDENADOS

num1 = int(input('Introduce el primer numero: '))
num2 = int(input('Introduce el segundo numero: '))
num3 = int(input('Introduce el tercer numero: '))
num4 = int(input('Introduce el cuarto numero: '))
num5 = int(input('Introduce el quinto numero: '))

if (num1 > num2) and (num2 > num3) and (num3 > num4) and (num4 > num5):
    print('El orden es decreciente')
elif (num1 < num2) and (num2 < num3) and (num3 < num4) and (num4 < num5):
    print('El orden es creciente')
else:
    print('Los números estan desordenados')
