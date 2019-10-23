# JOSE MANUEL - P5E12 - ESCRIBE UN PROGRAMA QUE PIDA UN NÚMERO Y ESCRIBA SI ES
# PRIMO O NO

num = int(input('Introduce un numero: '))
mensaje = 'es primo'
for i in range(2, num):
    if (num % i == 0):
        mensaje = 'no es primo'

print(mensaje)
    
    
        

