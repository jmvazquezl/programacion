# JOSE MANUEL - P4E3 - CALCULAR EL AREA DE UN TRIANGULO O UN CUADRADO

calc = int(input('Quieres calcular el area de un triangulo(1) o un cuadrado(2): '))

if (calc == 2):
    long = int(input('Introduce la longitud del lado del cuadrado: '))
    area = long * long
    print('El area del cuadrado es', area, '')

elif (calc == 1):
    base = int(input('Introduce la base del triangulo: '))
    altura = int(input('Introduce la base del triangulo: '))
    area2 = (base * altura) / 2
    print('El area del triangulo es', area2, '')    
