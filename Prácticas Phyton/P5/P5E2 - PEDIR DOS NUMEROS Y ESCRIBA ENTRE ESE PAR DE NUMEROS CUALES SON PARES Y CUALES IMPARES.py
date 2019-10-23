# JOSE MANUEL - P5E2 - PROGRAMA QUE PIDA DOS NUMEROS Y ESCRIBA QUE NUMEROS ENTRE ESE PAR
# SON PARES E INPARES

num1 = int(input('Escribe el primer numero: '))
num2 = int(input('Escribe el segundo numero: '))

for i in range(num1, num2 + 1):
    if (i % 2 == 0):
        print('El número', i, 'es par')
    else:
        print('El número', i, 'es impar')
