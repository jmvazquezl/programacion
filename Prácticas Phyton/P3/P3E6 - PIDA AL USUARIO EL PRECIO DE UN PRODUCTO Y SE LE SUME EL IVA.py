# JOSE MANUEL - P3E6 - PIDA AL USUARIO EL PRECIO DE UN PRODUCTO Y EL NOMBRE DE
# DEL PRODUCTO Y MUESTRE EL MENSAJE CON EL PRECIO DEL IVA (21%)

precio = float(input('Introduce el precio de tu producto: '))

iva = precio * float(0.21)

total = precio + iva

print ('Tu producto vale',precio,'y con el 21% de IVA \
se queda en',total,'en total')

