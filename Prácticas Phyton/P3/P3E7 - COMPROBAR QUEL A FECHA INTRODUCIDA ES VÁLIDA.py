# JOSE MANUEL - P3E7 - COMPROBAR QUE LA FECHA INTRODUCIDA ES VÁLIDA

dia = int(input('Introduce el dia: '))
mes = int(input('Introduce el mes: '))
año = int(input('Introduce el año: '))

if (año <= 0) or (mes >= 13) or (mes <= 0) or (dia >= 32) or (dia <= 0):
    print('', dia, '/', mes, '/', año, ' ES UNA FECHA CORRECTA')

elif (mes == 2):
    if (dia > 28) or (dia <= 0):
        print('', dia, '/', mes, '/', año, ' ES UNA FECHA CORRECTA')

    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        if (dia > 30) or (dia <= 0):
            print('', dia, '/', mes, '/', año, ' ES UNA FECHA CORRECTA')

else:
    print('', dia, '/', mes, '/', año, ' ES UNA FECHA CORRECTA')
        
    

