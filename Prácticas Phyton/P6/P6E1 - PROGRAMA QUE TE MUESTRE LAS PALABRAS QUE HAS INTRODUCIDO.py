# JOSE MANUEL - P6E1 - PROGRAMA QUE TE MUESTRE LAS PALABRAS QUE HAS INTRODUCIDO. PARA SALIR
# PULSAR ENTER

palabras=[]
i=str(input("Introduce una palabra: "))

while i:
    palabras.append(i)
    i=str(input("Introduce una palabra mas: "))

print ("Las palabras que has escrito son:",palabras,)
