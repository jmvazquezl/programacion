# JOSE MANUEL - P3E5 - PIDA UN NÚMERO COMO MÁXIMO DE 3 CIFRAS.SI SE INTRODUCE
# UN NÚMERO MAYOR QUE SALGA UN MENSAJE DE ERROR.

num = int(input('Introduce un número: '))

if (num < 1000) and (num > -1000):
    print ('El numero',num,'es valido')
else:
    print ('ERROR: El número',num,'tiene más de tres cifras')


