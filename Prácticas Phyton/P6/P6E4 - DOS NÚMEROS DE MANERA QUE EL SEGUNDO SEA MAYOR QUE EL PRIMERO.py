# JOSE MANUEL - P6E4 - DOS NÚMEROS DE MANERA QUE EL SEGUNDO SEA MAYOR QUE EL
# PRIMERO

num1 = int(input('Introduce un número: '))
print('Introduce un número mayor que', num1, '', end='')
num2 = int(input(":"))

while num1 + 1 > num2:
    print('', num2, 'No es mayor que', num1, '', end='')
    num2 = int(input('.Vuelve a introducir un numero:'))

print('Los numeros que has introducidos son',num1,'y',num2,)
