# JOSE MANUEL - P4E5 - IMPORTE EN EUROS Y DIGA SI EL CAJERO AUTOMATICO LE PUEDE
# DAR DICHO IMPORTE UTILIZANDO EL MISMO BILLETE Y EL MÁS GRANDE

importe = int(input("Introduce el importe que quieres sacar: "))

if (importe % 500 == 0):
    cantidad = importe // 500
    print('', importe, 'el cajero te devuelve', cantidad, 'billete de 500')

elif (importe % 200 == 0):
    cantidad = importe // 200
    print('', importe, 'el cajero te devuelve', cantidad, 'billete de 200')

elif (importe % 100 == 0):
    cantidad = importe // 100
    print('', importe, 'el cajero te devuelve', cantidad, 'billete de 100')

elif (importe % 50 == 0):
    cantidad = importe // 50
    print('', importe, 'el cajero te devuelve', cantidad, 'billete de 50')

elif (importe % 20 == 0):
    cantidad = importe // 20
    print('', importe, 'el cajero te devuelve', cantidad, 'billetes de 20')

elif (importe % 10 == 0):
    cantidad = importe // 10
    print('', importe, 'el cajero te devuelve', cantidad, 'billete de 10')

elif (importe % 5 == 0):
    cantidad = importe // 5
    print('', importe, 'el cajero te devuelve', cantidad, 'billete de 5')
